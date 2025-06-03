from graphics import Window, Line, Point


def main():
    win = Window(800, 600)
    l = Line(Point(40, 70), Point(760, 530))
    win.draw_line(l, "black")
    win.wait_for_close()


main()
