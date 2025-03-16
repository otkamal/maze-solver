import time
import constants
from cell import Point, Line, Cell, Window

class Maze:
    def __init__(
            self,
            window: Window,
            position: Point,
            num_rows: int,
            num_cols: int,
            cell_size_x: int = 35,
            cell_size_y: int = 35,
        ):

        self.__cells = []
        self.__position = position
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__window = window

        self.__create_cells()

    def __create_cells(self):
        current_position = self.__position
        for i in range(self.__num_cols):
            column = []
            for j in range(self.__num_rows):
                relative_bottom_left = current_position + Point(self.__cell_size_x, self.__cell_size_y)
                column.append(
                    Cell(
                        self.__window,
                        current_position,
                        relative_bottom_left
                    )
                )
                current_position += Point(0, self.__cell_size_y)
            current_position = self.__position + Point(self.__cell_size_x * (i + 1), 0)
            self.__cells.append(column)
            
    def __draw_cell(self, i: int, j: int):
        self.__cells[i][j].draw(constants.MAZE_LINE_COLOR, constants.MAZE_LINE_WIDTH)
        self.__animate()

    def __animate(self):
        self.__window.redraw()
        time.sleep(0.05)