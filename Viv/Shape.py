import turtle as t
from random import random


def DrawTriAngle(sides, length):

    for _ in range(sides):
        t.forward(length)
        t.left(360 / sides)  # 꼭지점 위로 향할 때
        # t.right(360 / sides) # 꼭지점 아래로 향할 때
    t.mainloop()


def DrawRectangle(width, height):

    screen = t.Screen()
    TURTLE_SIZE = 20
    t.hideturtle()
    t.penup()
    t.goto(
        (TURTLE_SIZE / 2) - (screen.window_width() / 2),
        (screen.window_height() / 2) - (TURTLE_SIZE / 2),
    )
    t.pendown()
    t.showturtle()
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.mainloop()


def DrawCircle(radius):

    t.circle(radius)
    t.mainloop()


def DrawEtc():
    t.home()
    t.pos()
    t.clearscreen()

    for steps in range(100):
        for c in ["red", "green", "blue"]:
            t.color(c)
            t.forward(steps)
            t.right(30)
    t.mainloop()


def DrawEtc2():
    t.color("red")
    t.begin_fill()
    while True:
        t.forward(300)
        t.left(170)
        if abs(t.pos()) < 1:
            break
    t.end_fill()
    t.mainloop()
