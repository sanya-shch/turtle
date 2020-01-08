import turtle
import random


def star_fill(n, l):
    tt.begin_fill()
    if n % 2 != 0:
        for i in range(n):
            tt.forward(l)
            angle = n // 2 * 360 / n
            tt.left(angle)
    tt.end_fill()


ts = turtle.Screen()
ts.bgcolor('black')
ts.setup(800, 600)

tt = turtle.Turtle()
tt.hideturtle()
tt.speed(20)
tt.color('yellow')


def move(x, y):
    tt.up()
    tt.setposition(x, y)
    tt.down()
    size = random.randint(10, 30)
    n = random.choice([5, 7, 9])
    star_fill(n, size)


ts.onclick(move)
ts.listen()
ts.mainloop()
