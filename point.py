class Point:
    def __init__(self, position_x: int, position_y: int):
        self.position_x = position_x
        self.position_y = position_y

    def __add__(self, other):
        return Point(
            self.position_x + other.position_x,
            self.position_y + other.position_y
        )

    def __str__(self):
        return f"({self.position_x, self.position_y})"

    def __eq__(self, other):
        self.position_x = other.position_x
        self.position_y = other.position_y