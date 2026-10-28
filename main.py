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
    maze = Maze(
        margin_x,
        margin_y,
        rows,
        columns,
        cell_size_x,
        cell_size_y,
        win,
        10
    )
 
    win.wait_for_close()


main()
        
