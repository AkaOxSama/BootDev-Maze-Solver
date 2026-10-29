import time

from graphics import Window
from maze import Maze


def main() -> None:
    # Size of the window
    window_width: int = 800
    window_height: int = 600
    # Margin of the borders of the window
    margin_x: int = 50
    margin_y: int = 50
    # Number of columns and rows
    columns: int = 20
    rows: int = 20
    # Size of the cells
    cell_size_x: float = (window_width - 2 * margin_x) / columns
    cell_size_y: float = (window_height - 2 * margin_y) / rows
    # Creation of the window
    win = Window(window_width, window_height)
    #Creation of the maze
    print("Maze created")
    maze = Maze(
        margin_x,
        margin_y,
        rows,
        columns,
        cell_size_x,
        cell_size_y,
        win,
        
    )
    # Wait an amount of time to see the maze
    time.sleep(1)
    # Solve the maze
    can_be_solved: bool = maze.solve()
    if can_be_solved:
        print("Maze Solved!")
    else:
        print("Maze can't be solved")
    # Close the window on exit
    win.wait_for_close()


main()
        
