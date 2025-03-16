ROOT_TITLE = "Maze Solver"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

MAZE_LINE_COLOR = "black"
MAZE_LINE_WIDTH = 2

CELL_ALL_WALLS = {"left": True, "right": True, "top": True, "bottom": True}
CELL_NO_WALLS = {"left": False, "right": False, "top": False, "bottom": False}
CELL_NO_LEFT = {"left": False, "right": True, "top": True, "bottom": True}
CELL_NO_RIGHT = {"left": True, "right": False, "top": True, "bottom": True}
CELL_NO_TOP = {"left": True, "right": True, "top": False, "bottom": True}
CELL_NO_BOTTOM = {"left": True, "right": True, "top": True, "bottom": False}