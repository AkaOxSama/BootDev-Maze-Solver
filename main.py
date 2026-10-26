from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    line = Line(Point(100, 100), Point(500, 200))
    win.draw_line(line, "red")
    win.wait_for_close()


if __name__ == "__main__":
    main()
        
