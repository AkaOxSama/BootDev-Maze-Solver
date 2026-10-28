import unittest

from maze import Maze

class Tests(unittest.TestCase):
    # Test creation of the maze
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
            m1.__win,
            None
        )
    def test_maze_create_cells_large(self):
        num_cols = 100
        num_rows = 120
        m1 = Maze(20, 20, num_rows, num_cols, 100, 100)
        self.assertEqual(
            len(m1._Maze__cells), # type: ignore
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]), # type: ignore
            num_rows,
        )

    # Test creation of entry and exit
    def test_maze_create_entry_exit(self):
        num_cols = 20
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 5, 5)
        m1.Maze__break_entrance_and_exit() #type: ignore
        self.assertEqual(
            m1.__cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1.__cells[num_rows - 1][num_cols - 1].has_bottom_wall,
            False,
        )
if __name__ == "__main__":
    unittest.main()