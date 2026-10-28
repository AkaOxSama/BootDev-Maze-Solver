from graphics import Window, Point, Line


class Cell:
    def __init__(self, window: Window|None = None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_botom_wall = True

        self.__x1 = -1.0
        self.__x2 = -1.0
        self.__y1 = -1.0
        self.__y2 = -1.0

        self.__win = window

    def draw(self, x1:float, y1:float, x2:float, y2:float) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        if self.__win is None:
            return
        
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(line)
        if self.has_botom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(line)

    def draw_move(self, to_cell: "Cell", undo: bool = False) -> None:
            half_self = abs(self.__x2 - self.__x1) // 2
            
            center_self_x = half_self + self.__x1
            center_self_y = half_self + self.__y1

            half_other = abs(to_cell.__x2 - to_cell.__x1) // 2

            center_other_x = half_other + to_cell.__x1
            center_other_y = half_other + to_cell.__y1

            line_color = ""
            if undo:
                 line_color = "gray"
            else:
                 line_color = "red"

            line = Line(Point(center_self_x, center_self_y), Point(center_other_x, center_other_y))
            if self.__win == None:
                return 
            self.__win.draw_line(line, fill_color=line_color)
