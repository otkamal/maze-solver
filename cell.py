from line import Point, Line
from window import Window

class Cell:
    def __init__(self,
                 window: Window, 
                 top_left: Point,
                 bottom_right: Point,
                 walls: dict = {"left": True, "right": True, "top": True, "bottom": True}):
        self.__top_left = top_left
        self.__bottom_right = bottom_right
        self.__window = window
        self.walls = walls

    def __str__(self):
        return f"Cell Object @ {self.__top_left} -> {self.__bottom_right}"

    def get_center(self) -> Point:
        return Point(
            (self.__top_left.position_x + self.__bottom_right.position_x) / 2,
            (self.__top_left.position_y + self.__bottom_right.position_y) / 2
        )
    
    def draw_move(self, to_cell, undo = False) -> None:
        color = "red"
        if undo:
            color = "gray"
        self.__window.draw_line(Line(self.get_center(), to_cell.get_center()), line_color=color, line_width=2)

    def draw(self, line_color: str, line_width: int) -> None:
        for wall in ["left", "right", "top", "bottom"]:
            if self.walls[wall]:
                match wall:
                    case "left":
                        line = Line(
                            self.__top_left,
                            Point(self.__top_left.position_x, self.__bottom_right.position_y)
                        )
                    case "right":
                        line = Line(
                            Point(self.__bottom_right.position_x, self.__top_left.position_y),
                            self.__bottom_right
                        )
                    case "top":
                        line = Line(
                            self.__top_left,
                            Point(self.__bottom_right.position_x, self.__top_left.position_y)
                        )
                    case "bottom":
                        line = Line(
                            Point(self.__top_left.position_x, self.__bottom_right.position_y),
                            self.__bottom_right
                        )

                self.__window.draw_line(line, line_color, line_width)

                