import turtle
import time
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

for i in range(15):
    tt.up()
    tt.setposition(random.randint(-350, 350), random.randint(-250, 250))
    tt.down()
    size = random.randint(10, 30)
    n = random.choice([5,7,9])
    star_fill(n, size)

time.sleep(2)
