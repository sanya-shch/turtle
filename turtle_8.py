import turtle
import random

ts = turtle.Screen()

border = turtle.Turtle()
border.speed(0)
border.up()
border.hideturtle()
border.pensize(4)
border.color('red')
border.goto(300,300)
border.down()
border.goto(300,-300)
border.goto(-300,-300)
border.goto(-300,300)
border.goto(300,300)

ball = turtle.Turtle()
ball.shape('circle')
ball.up()

rand_x = random.randint(-290,290)
rand_y = random.randint(-290,290)
ball.hideturtle()
ball.goto(rand_x,rand_y)
ball.showturtle()

dx = 1
dy = 1

while True:
    x,y = ball.position()
    if x+dx >= 300 or x+dx <= -300:
        dx *= -1
    if y+dy >= 300 or y+dy <= -300:
        dy *= -1
    ball.goto(x+dx, y+dy)
