from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__is_running = False
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__is_running = True

        while self.__is_running:
            self.redraw()
        print("window closed...")

    def close(self) -> None:
        self.__is_running = False

    def draw_line(self, line: "Line", fill_color:str = "black") -> None:
        line.draw(self.__canvas, fill_color)


# Classes for lines        

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_a: Point, point_b: Point) -> None:
        self.point_a: Point = point_a
        self.point_b: Point = point_b

    def draw(self, canvas: Canvas, fill_color: str = "black") -> None:
        canvas.create_line(self.point_a.x, self.point_a.y, self.point_b.x, self.point_b.y, fill=fill_color, width=2)


