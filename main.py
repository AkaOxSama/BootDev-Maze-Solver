from graphics import Window
from cells import Cell

def main():
    win = Window(800, 600)
    c1 = Cell(win)
    c1.draw(50,50, 100, 100)

    c2 = Cell(win)
    c2.draw(100, 50, 150, 100)

    c1.draw_move(c2, undo=True)
    win.wait_for_close()



main()
        
