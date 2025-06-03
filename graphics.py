from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )


class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1, x2, y1, y2):
        if self.__win is None:
            return
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        no_wall_color = "red"

        left_wall_line = Line(Point(self.__x1, self.__y2), Point(self.__x1, self.__y1))
        if self.has_left_wall:
            self.__win.draw_line(left_wall_line)
        else:
            self.__win.draw_line(left_wall_line, no_wall_color)
        
        top_wall_line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
        if self.has_top_wall:
            self.__win.draw_line(top_wall_line)
        else:
            self.__win.draw_line(top_wall_line, no_wall_color)
        
        right_wall_line = Line(Point(self.__x2, self.__y2), Point(self.__x2, self.__y1))
        if self.has_right_wall:
            self.__win.draw_line(right_wall_line)
        else:
            self.__win.draw_line(right_wall_line, no_wall_color)
        
        bottom_wall_line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
        if self.has_bottom_wall:
            self.__win.draw_line(bottom_wall_line)
        else:
            self.__win.draw_line(bottom_wall_line, no_wall_color)
    
    def draw_move(self, to_cell, undo=False):
        line = Line(
            Point(self.center_of_cell()[0], self.center_of_cell()[1]), 
            Point(to_cell.center_of_cell()[0], to_cell.center_of_cell()[1]),
        )
        print(self.center_of_cell()[0], self.center_of_cell()[1],to_cell.center_of_cell()[0], to_cell.center_of_cell()[1])
        
        fill_color = "red"
        if undo:
            fill_color = "gray"
        
        if self.__win is None:
            return
        self.__win.draw_line(line, fill_color)
        
    def center_of_cell(self):
        x = (self.__x1 + self.__x2) // 2
        y = (self.__y1 + self.__y2) // 2
        return x, y