import time
import constants
import random
from cell import Point, Line, Cell, Window

class Maze:
    def __init__(
            self,
            window: Window,
            position: Point,
            num_rows: int,
            num_cols: int,
            cell_size_x: int = 25,
            cell_size_y: int = 25,
        ):

        self.cells = []
        self.__position = position
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__window = window

        self.__create_cells()

    def draw(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def solve(self):
        self.__solve_r(0, 0)

    def __create_cells(self):
        current_position = self.__position
        for i in range(self.__num_cols):
            column = []
            for j in range(self.__num_rows):
                relative_bottom_left = current_position + Point(self.__cell_size_x, self.__cell_size_y)
                column.append(
                    {
                        "cell": Cell(
                            self.__window,
                            current_position,
                            relative_bottom_left
                        ),
                        "visited": False
                    }
                )
                current_position += Point(0, self.__cell_size_y)
            current_position = self.__position + Point(self.__cell_size_x * (i + 1), 0)
            self.cells.append(column)
            
    def __draw_cell(self, i: int, j: int):
        self.cells[i][j]["cell"].draw(constants.MAZE_LINE_COLOR, constants.MAZE_LINE_WIDTH)
        self.__animate()

    def __break_entrance_and_exit(self):
        self.cells[0][0]["cell"].walls["top"] = False
        self.__draw_cell(0, 0)

        self.cells[self.__num_cols - 1][self.__num_rows - 1]["cell"].walls["bottom"] = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, i, j):
        self.cells[i][j]["visited"] = True
        while True:
            possible_moves = []
            top = (i, j - 1)
            bottom = (i, j + 1)
            left = (i - 1, j)
            right = (i + 1, j)
            
            for dir in [top, bottom, left, right]:
                x = dir[0]
                y = dir[1]
                # make sure valid index
                if 0 <= x < self.__num_cols and 0 <= y < self.__num_rows:
                    if not self.cells[x][y]["visited"]:
                        possible_moves.append(dir)
            
            if not possible_moves:
                self.__draw_cell(i, j)
                break

            next_cell = random.choice(possible_moves)

            if next_cell == top:
                self.cells[i][j]["cell"].walls["top"] = False
                self.cells[i][j - 1]["cell"].walls["bottom"] = False
            elif next_cell == bottom:
                self.cells[i][j]["cell"].walls["bottom"] = False
                self.cells[i][j + 1]["cell"].walls["top"] = False
            elif next_cell == left:
                self.cells[i][j]["cell"].walls["left"] = False
                self.cells[i - 1][j]["cell"].walls["right"] = False
            elif next_cell == right:
                self.cells[i][j]["cell"].walls["right"] = False
                self.cells[i + 1][j]["cell"].walls["left"] = False

            self.__break_walls_r(next_cell[0], next_cell[1])

    def __reset_cells_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.cells[i][j]["visited"] = False

    def __get_exit(self):
        return (self.__num_cols - 1, self.__num_rows - 1)
    
    def __solve_r(self, i, j):
        self.__animate()
        self.cells[i][j]["visited"] = True
        if (i, j) == self.__get_exit():
            return True
        
        top = (i, j - 1)
        bottom = (i, j + 1)
        left = (i - 1, j)
        right = (i + 1, j)

        directions = [top, bottom, left, right]
        labels = ["top", "bottom", "left", "right"]
        for d in range(len(directions)):
            x = directions[d][0]
            y = directions[d][1]
            dir = labels[d]
            if 0 <= x < self.__num_cols and 0 <= y < self.__num_rows:
                current_cell = self.cells[i][j]["cell"]
                neighbor = self.cells[x][y]["cell"]
                if current_cell.is_connected(dir, neighbor) and not self.__is_cell_visited(x, y):
                    current_cell.draw_move(neighbor)
                    status = self.__solve_r(x, y)
                    if status:
                        return True
                    
                    current_cell.draw_move(neighbor, undo = True)

        return False

    def __is_cell_visited(self, i, j):
        return self.cells[i][j]["visited"]
            
    def __animate(self):
        self.__window.redraw()
        time.sleep(0.025)