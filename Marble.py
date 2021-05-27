'''
   CS5001
   Spring 2021
   Chiayin Fan
   Class of Marble
'''
import turtle
from Point import Point

MARBLE_RADIUS = 20


class Marble:
    def __init__(self, position, color, size=MARBLE_RADIUS):
        self.pen = self.new_pen()
        self.color = color
        self.position = position
        self.visible = False
        self.is_empty = True
        self.pen.hideturtle()
        self.size = size
        self.pen.speed(0)  # set to fastest drawing

    def new_pen(self):
        return turtle.Turtle()

    def set_color(self, color):
        self.color = color
        self.is_empty = False

    def get_color(self):
        return self.color

    def draw(self):
        # if self.visible and not self.is_empty:
        # return
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.visible = True
        self.is_empty = False
        self.pen.down()
        self.pen.fillcolor(self.color)
        self.pen.begin_fill()
        self.pen.circle(self.size)
        self.pen.end_fill()

    def draw_empty(self):
        self.erase()
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.visible = True
        self.is_empty = True
        self.pen.down()
        self.pen.circle(self.size)

    def erase(self):
        self.visible = False
        self.pen.clear()

    def clicked_in_region(self, x, y):
        # Since self.position.x and self.position.y is not the center of the circle,
        # the condition of the if statement is rewrite.
        if abs(x - self.position.x) <= self.size and \
                0 <= y - self.position.y <= self.size * 2:
            return True
        return False

    def __str__(self):
        return self.color


def main():
    marble_1 = Marble(Point(100, 100), "red")
    marble_1.draw_empty()
    marble_1.draw()
    marble_2 = Marble(Point(100, 200), "blue")
    marble_2.draw()
    asd = input('enter anything')
    marble_1.erase()
    turtle.done()


if __name__ == "__main__":
    main()
