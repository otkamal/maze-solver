import constants
from cell import Point, Line, Cell
from window import Window

def main() -> int:
    win = Window(constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
    cell_a = Cell(win, Point(50, 50), Point(100, 100))
    cell_b = Cell(win, Point(50, 150), Point(100, 200))
    cell_a.draw("black", 2)
    cell_b.draw("black", 2)
    cell_a.draw_move(cell_b, True)
    win.wait_for_close()
    return 0

if __name__ == "__main__":
    main()