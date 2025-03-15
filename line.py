from point import Point
from tkinter import Canvas

class Line:
    def __init__(self, point_a: Point, point_b: Point):
        self.point_a = point_a
        self.point_b = point_b
        
    def draw(self, canvas: Canvas, fill_color: str, line_width: int) -> None:
        canvas.create_line(
            self.point_a.position_x,
            self.point_a.position_y,
            self.point_b.position_x,
            self.point_b.position_y,
            fill = fill_color,
            width = line_width
        )   