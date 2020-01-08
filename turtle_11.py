import turtle
import random

ts = turtle.Screen()

border = turtle.Turtle()
border.speed(0)
border.up()
border.hideturtle()
border.pensize(4)
border.color('red')
border.goto(250, 250)
border.down()
border.goto(250, -250)
border.goto(-250, -250)
border.goto(-250, 250)

balls = []
count = 5
forms = ['circle', 'turtle', 'triangle', 'square']

for i in range(count):
    ball = turtle.Turtle(shape=random.choice(forms))
    ball.up()
    red = random.random()
    blue = random.random()
    green = random.random()
    ball.color(red, blue, green)
    rand_x = random.randint(-245, 245)
    rand_y = random.randint(0, 250)
    ball.goto(rand_x, rand_y)
    ball.speed_y = 0
    ball.speed_x = -2
    balls.append(ball)

gravitation = 0.1

while True:
    for ball in balls:
        ball.speed_y -= gravitation
        ball.goto(ball.xcor() + ball.speed_x, ball.ycor() + ball.speed_y)

        if ball.ycor() <= -250:
            ball.speed_y *= -1
        if ball.xcor() <= -250 or ball.xcor() >= 250:
            ball.speed_x *= -1
