from graphics import Window
from cells import Cell
import time

class Maze:
    def __init__(
            self,
            x1:float,
            y1:float,
            num_rows:int,
            num_cols:int,
            cell_size_x:float,
            cell_size_y:float,
            win: Window,
    ) -> None:
        self.x: float = x1
        self.y: float = y1
        self.rows: int = num_rows
        self.cols: int = num_cols
        self.size_x: float = cell_size_x
        self.size_y: float = cell_size_y
        self._win: Window = win

        self.__cells: list[list[Cell]] = []
        self.__create_cells()

    def __create_cells(self) -> None:
        cell = Cell(self._win)
        for i in range(self.cols):
            self.__cells.append([])
            for j in range(self.rows):
                self.__cells[i].append(cell)

        for c in range(self.cols):
            for r in range(self.rows):
                self.__draw_cell(c, r)

    def __draw_cell(self, column: int, row: int) -> None:
        x1: float = self.x + (row * self.size_x)
        y1: float = self.y + (column * self.size_y)
        x2: float = x1 + self.size_x
        y2: float = y1 + self.size_y

        self.__cells[column][row].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self) -> None:
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.005)
        