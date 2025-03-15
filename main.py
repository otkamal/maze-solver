import constants
from point import Point
from line import Line
from window import Window

def main() -> int:
    win = Window(constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
    win.draw_line(Line(Point(100, 200), Point(100, 100)), "black", 2)
    win.wait_for_close()
    return 0

if __name__ == "__main__":
    main()