import turtle

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

ball = turtle.Turtle(shape='circle')
ball.up()
ball.goto(0, 230)
ball.speed_y = 0
ball.speed_x = -2

gravitation = 0.1

while True:
    ball.speed_y -= gravitation
    ball.goto(ball.xcor() + ball.speed_x, ball.ycor() + ball.speed_y)

    if ball.ycor() <= -250:
        ball.speed_y *= -1
    if ball.xcor() <= -250 or ball.xcor() >= 250:
        ball.speed_x *= -1
