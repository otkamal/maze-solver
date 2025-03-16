import unittest
from maze import Window, Point, Maze

class Test(unittest.TestCase):
    def test_maze_create_cells_same(self):
        num_cols = 12
        num_rows = 12
        m1 = Maze(
            Window(0, 0),
            Point(0, 0),
            num_rows,
            num_cols
        )
        self.assertEqual(
            len(m1.cells),
            num_cols
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows
        )

    def test_maze_create_cells_diff(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(
            Window(0, 0),
            Point(0, 0),
            num_rows,
            num_cols
        )
        self.assertEqual(
            len(m1.cells),
            num_cols
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows
        )

if __name__ == "__main__":
    unittest.main()