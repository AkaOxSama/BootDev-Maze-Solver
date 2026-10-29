import unittest

from maze import Maze

class Tests(unittest.TestCase):
    # Test creation of the maze
    def test_maze_create_cells(self) -> None:
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(getattr(m1, "_Maze__cells")),
            num_cols,
        )
        self.assertEqual(
            len(getattr(m1, "_Maze__cells")[0]),
            num_rows,
        )


    # Test creation of entry and exit
    def test_maze_create_entry_exit(self) -> None:
        num_cols = 20
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 5, 5)
        self.assertEqual(
            getattr(m1, "_Maze__cells")[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            getattr(m1, "_Maze__cells")[num_rows - 1][num_cols - 1].has_bottom_wall,
            False,
        )

    # Test checking all cells false after breaking of walls
    def test_maze_check_false_visited(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0,0, num_rows, num_cols, 5, 5)

        false_count = 0
        for col in getattr(m1, "_Maze__cells"):
            for row in col:
                    false_count += 1

        self.assertEqual(
            false_count,
            100
        )

if __name__ == "__main__":
    unittest.main()