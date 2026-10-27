from graphics import Window
from cells import Cell

def main():
    win = Window(800, 600)
    c1 = Cell(win)
    c1.draw(50,50, 100, 100)

    c2 = Cell(win)
    c2.has_right_wall = False
    c2.draw(250, 250, 400, 400)
    win.wait_for_close()



main()
        
