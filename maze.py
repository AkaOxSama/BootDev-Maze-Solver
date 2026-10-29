import time
import random

from cells import Cell
from graphics import Window


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: float,
        cell_size_y: float,
        win: Window | None = None,
        seed: int | None = None
    ) -> None:
        self.__cells: list[list[Cell]] = []
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

        if seed is not None:
            random.seed(seed)

    # Create the grid of cells on the window
    def __create_cells(self) -> None:
        for i in range(self.__num_cols):
            col_cells: list[Cell] = []
            for j in range(self.__num_rows):
                col_cells.append(Cell(self.__win))
            self.__cells.append(col_cells)
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    # Draws the cell itself
    def __draw_cell(self, i: int, j: int) -> None:
        if self.__win is None:
            return
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()

    # Creates an animation for visual purposes (cost performance)
    def __animate(self) -> None:
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.005)

    # Creates an entrance and an exit on the grid
    def __break_entrance_and_exit(self) -> None:
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    # Creates a random path between the cells in the maze
    def __break_walls_r(self, i: int, j: int) -> None:
        self.__cells[i][j].visited = True

        while True:
            visited = []

            # Check left
            if i > 0 and not self.__cells[i - 1][j].visited:
                visited.append((i - 1, j))
            # Check right
            if i < self.__num_cols - 1 and not self.__cells[i + 1][j].visited:
                visited.append((i + 1, j))
            # Check top
            if j > 0 and not self.__cells[i][j - 1].visited:
                visited.append((i, j - 1))
            if j < self.__num_rows - 1 and not self.__cells[i][j + 1].visited:
                visited.append((i, j + 1))
            # Check bottom
            if len(visited) == 0:
                self.__draw_cell(i, j)
                return

            direction_index: int = random.randrange(len(visited))
            next_to_visit = visited[direction_index]
            # Go right
            if next_to_visit[0] == i + 1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[i + 1][j].has_left_wall = False
            # Go left
            if next_to_visit[0] == i - 1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[i - 1][j].has_right_wall = False
            # Go up
            if next_to_visit[1] == j - 1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j - 1].has_bottom_wall = False
            # Go bottom
            if next_to_visit[1] == j + 1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j + 1].has_top_wall = False

            self.__break_walls_r(next_to_visit[0], next_to_visit[1])

    # Resets the visited attribute of all the cell so we can solve it
    def __reset_cells_visited(self) -> None:
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__cells[i][j].visited = False

    # Method to solve the maze
    def solve(self) -> bool:
        return self._solve_r(0, 0)
    # The maze solver
    def _solve_r(self, i: int, j: int) -> bool:
        self.__animate()

        self.__cells[i][j].visited = True

        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            return True

        # Check left to right
        if i < self.__num_cols - 1 and not self.__cells[i + 1][j].visited and not self.__cells[i][j].has_right_wall:
            self.__cells[i][j].draw_move(self.__cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
               self.__cells[i][j].draw_move(self.__cells[i + 1][j], undo=True)

        # Check right to left
        if i > 0 and not self.__cells[i - 1][j].visited and not self.__cells[i][j].has_left_wall: 
            self.__cells[i][j].draw_move(self.__cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i - 1][j], undo=True)

        # Check top to bottom
        if j < self.__num_rows - 1 and not self.__cells[i][j + 1].visited and not self.__cells[i][j].has_bottom_wall:
            self.__cells[i][j].draw_move(self.__cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j + 1], undo=True)

        # Check bottom to top
        if j > 0 and not self.__cells[i][j - 1].visited and not self.__cells[i][j].has_top_wall:
            self.__cells[i][j].draw_move(self.__cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j - 1], undo=True)


        return False


            