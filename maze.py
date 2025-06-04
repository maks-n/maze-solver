import time
import random
from graphics import Cell


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = [[0 for _ in range(self.__num_rows)] for _ in range(self.__num_cols)]

        if seed:
            random.seed(seed)

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def __create_cells(self):
        for col in range (self.__num_cols):
            for row in range(self.__num_rows):
                self.__cells[col][row] = Cell(self.__win)
                self.__draw_cell(col, row)
    
    
    def __draw_cell(self, i, j):
        x1 = self.__x1 + self.__cell_size_x * i
        x2 = x1 + self.__cell_size_x
        y1 = self.__y1 + self.__cell_size_y * j
        y2 = y1 + self.__cell_size_y
        self.__cells[i][j].draw(x1, x2, y1, y2)
        self.__animate()
    
    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.00005)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols-1][self.__num_rows-1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols-1, self.__num_rows-1)

    def __break_walls_r(self, col, row):
        self.__cells[col][row].visited = True
        
        while True:
            to_visit = []
            # to visit next
            # left
            if col > 0 and not self.__cells[col - 1][row].visited:
                to_visit.append((col - 1, row))
            # right
            if col < self.__num_cols - 1 and not self.__cells[col + 1][row].visited:
                to_visit.append((col + 1, row))
            # up
            if row > 0 and not self.__cells[col][row - 1].visited:
                to_visit.append((col, row - 1))
            # down
            if row < self.__num_rows - 1 and not self.__cells[col][row + 1].visited:
                to_visit.append((col, row + 1))
            
            if len(to_visit) == 0:
                self.__draw_cell(col, row)
                return
            
            random_index = random.randrange(len(to_visit))
            next_index = to_visit[random_index]
            
            # break wall between current and next cells
            # right
            if next_index[0] == col + 1:
                self.__cells[col][row].has_right_wall = False
                self.__cells[col + 1][row].has_left_wall = False
            # left
            if next_index[0] == col - 1:
                self.__cells[col][row].has_left_wall = False
                self.__cells[col - 1][row].has_right_wall = False
            # down
            if next_index[1] == row + 1:
                self.__cells[col][row].has_bottom_wall = False
                self.__cells[col][row + 1].has_top_wall = False
            # up
            if next_index[1] == row - 1:
                self.__cells[col][row].has_top_wall = False
                self.__cells[col][row - 1].has_bottom_wall = False
            
            self.__break_walls_r(next_index[0], next_index[1])

    def __reset_cells_visited(self):
        for col in self.__cells:
            for cell in col:
                cell.visited = False
    
    def solve(self):
        return self.__solve_r(0, 0)

    def __solve_r(self, col, row):
        self.__animate()
        
        self.__cells[col][row].visited = True

        if col == self.__num_cols - 1 and row == self.__num_rows - 1:
            return True
        
        # right
        if (
            col < self.__num_cols - 1
            and not self.__cells[col][row].has_right_wall 
            and not self.__cells[col + 1][row].visited
        ):
            self.__cells[col][row].draw_move(self.__cells[col + 1][row])
            if self.__solve_r(col + 1, row):
                return True
            else:
                self.__cells[col][row].draw_move(self.__cells[col + 1][row], True)
        # left
        if (
            col > 0
            and not self.__cells[col][row].has_left_wall 
            and not self.__cells[col - 1][row].visited
        ):
            self.__cells[col][row].draw_move(self.__cells[col - 1][row])
            if self.__solve_r(col - 1, row):
                return True
            else:
                self.__cells[col][row].draw_move(self.__cells[col - 1][row], True)
        # up
        if (
            row > 0
            and not self.__cells[col][row].has_top_wall 
            and not self.__cells[col][row - 1].visited
        ):
            self.__cells[col][row].draw_move(self.__cells[col][row - 1])
            if self.__solve_r(col, row - 1):
                return True
            else:
                self.__cells[col][row].draw_move(self.__cells[col][row - 1], True)
        # down
        if (
            row < self.__num_rows - 1
            and not self.__cells[col][row].has_bottom_wall 
            and not self.__cells[col][row + 1].visited
        ):
            self.__cells[col][row].draw_move(self.__cells[col][row + 1])
            if self.__solve_r(col, row + 1):
                return True
            else:
                self.__cells[col][row].draw_move(self.__cells[col][row + 1], True)
        
        return False
                

