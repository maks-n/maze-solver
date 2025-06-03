from graphics import Window, Line, Point, Cell
from maze import Maze

def main():
    win = Window(800, 600)
    
    Maze(10, 10, 20, 30, 20, 20, win)
    
    win.wait_for_close()


main()
