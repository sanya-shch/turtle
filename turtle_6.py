import turtle

ts = turtle.Screen()
tt = turtle.Turtle()

l = 10


def move_up():
    x, y = tt.position()
    tt.setposition(x, y + l)


def move_down():
    x, y = tt.position()
    tt.setposition(x, y - l)


def move_left():
    x, y = tt.position()
    tt.setposition(x - l, y)


def move_right():
    x, y = tt.position()
    tt.setposition(x + l, y)


def change():
    if tt.isvisible():
        tt.up()
        tt.hideturtle()
    else:
        tt.down()
        tt.showturtle()


def len_up():
    global l
    l += 10


def len_down():
    global l
    l -= 10


ts.onkey(move_up, "Up")
ts.onkey(move_down, "Down")
ts.onkey(move_left, "Left")
ts.onkey(move_right, "Right")
ts.onkey(change, "space")
ts.onkey(len_up, "+")
ts.onkey(len_down, "-")


ts.listen()
ts.mainloop()
