from graphics import Window, Line, Point, Cell
from maze import Maze

def main():
    win = Window(800, 600)
    
    maze = Maze(10, 10, 10, 15, 30, 30, win)
    maze._Maze__break_entrance_and_exit()
    
    win.wait_for_close()


main()
