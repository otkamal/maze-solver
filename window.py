import constants
from line import Line
from tkinter import Tk, Canvas

class Window:
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.geometry(f"{width}x{height}")
        self.__root.title(constants.ROOT_TITLE)
        self.__canvas = Canvas()
        self.__canvas.pack(fill = "both", expand = True)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self) -> None:
        self.__running = False

    def draw_line(self, line: Line, line_color: str, line_width: int) -> None:
        line.draw(self.__canvas, line_color, line_width)