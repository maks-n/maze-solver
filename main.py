from graphics import Window, Line, Point, Cell


def main():
    win = Window(800, 600)
    
    c = Cell(win)
    c.has_left_wall = False
    c.draw(10, 50, 10, 50)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(100, 200, 100, 200)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(300, 250, 300, 250)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(400, 500, 400, 500)
    
    c = Cell(win)
    c.draw(550, 700, 10, 500)
    
    win.wait_for_close()


main()
