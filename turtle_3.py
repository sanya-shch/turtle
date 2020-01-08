import turtle
import time

tt = turtle.Turtle()


def star_fill(n, l):
    tt.begin_fill()
    star(n, l)
    tt.end_fill()


def star(n, l):
    if n % 2 != 0:
        for i in range(n):
            tt.forward(l)
            angle = n // 2 * 360 / n
            tt.left(angle)


for i in range(5, 16, 2):
    tt.speed(10)
    star_fill(9, 150)
    time.sleep(2)
    tt.reset()

