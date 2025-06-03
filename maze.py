import time
from graphics import Cell


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = [[0 for _ in range(self.__num_rows)] for _ in range(self.__num_cols)]
        
        self.__create_cells()

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
        time.sleep(0.05)
