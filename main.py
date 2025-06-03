from graphics import Window, Line, Point, Cell


def main():
    win = Window(800, 600)
    
    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(100, 200, 100, 200)
    
    c2 = Cell(win)
    c2.has_left_wall = False
    c2.has_right_wall = False
    c2.draw(200, 360, 100, 200)

    c1.draw_move(c2)

    c3 = Cell(win)
    c3.has_left_wall = False
    c3.has_bottom_wall = False
    c3.draw(360, 400, 100, 200)
    
    c2.draw_move(c3)
    
    c4 = Cell(win)
    c4.has_top_wall = False
    c4.draw(360, 400, 200, 500)
    
    c3.draw_move(c4)
    
    win.wait_for_close()


main()
