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

balls = []
count = 10
for i in range(count):
    ball = turtle.Turtle()
    ball.shape('circle')
    ball.hideturtle()
    ball.up()
    rand_x = random.randint(-290,290)
    rand_y = random.randint(-290,290)
    ball.goto(rand_x,rand_y)
    ball.showturtle()
    dx = random.randint(-5,5)
    dy = random.randint(-5,5)
    balls.append([ball, dx, dy])

while True:
    # for i in balls:
    #     ball, dx, dy = i
    #     x,y = ball.position()
    #     if x+dx >= 300 or x+dx <= -300:
    #         i[1] *= -1
    #     if y+dy >= 300 or y+dy <= -300:
    #         i[2] *= -1
    #     ball.goto(x+dx, y+dy)
    for i in range(count):
        x,y = balls[i][0].position()
        if x+balls[i][1] >= 300 or x+balls[i][1] <= -300:
            balls[i][1] *= -1
        if y+balls[i][2] >= 300 or y+balls[i][2] <= -300:
            balls[i][2] *= -1
        balls[i][0].goto(x+balls[i][1], y+balls[i][2])
