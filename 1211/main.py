import graphics as gf
import random as rd

colors = ["red", "blue", "green", "orange", "yellow", "black"]


def main():
    win = gf.GraphWin("", 400, 350)

    c = gf.Circle(gf.Point(100, 150), 10)
    c.setFill("red")
    c.draw(win)

    while True:
        mouse_pos = win.getMouse()
        print(mouse_pos.getX(), mouse_pos.getY())

        color = rd.randint(0, len(colors) - 1)

        c = gf.Circle(mouse_pos, 10)
        c.setFill(colors[color])
        c.draw(win)


if __name__ == "__main__":
    main()
