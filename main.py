import constants
from maze import Point, Maze
from window import Window

def main() -> int:
    window = Window(constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
    maze = Maze(window, Point(10, 10), 15, 30)
    maze.draw()
    window.wait_for_close()
    return 0

if __name__ == "__main__":
    main()