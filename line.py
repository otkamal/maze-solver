from point import Point
from tkinter import Canvas

class Line:
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b
        
    def draw(self, canvas, fill_color, line_width):
        canvas.create_line(
            self.point_a.position_x,
            self.point_a.position_y,
            self.point_b.position_x,
            self.point_b.position_y,
            fill = fill_color,
            width = line_width
        )   