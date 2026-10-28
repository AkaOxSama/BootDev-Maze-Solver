import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells), # type: ignore
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]), # type: ignore
            num_rows,
        )
    def test_maze_create_cells_null(self) -> None:
        num_cols = 20
        num_rows = 20
        m1 = Maze(10,10, num_cols, num_rows, 10, 10)
        self.assertEqual(
            m1._win,
            None
        )


if __name__ == "__main__":
    unittest.main()