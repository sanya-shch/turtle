import turtle

tt = turtle.Turtle()
tt.speed(10)

tt.up()
tt.setposition(-50, -50)
tt.down()


def polygon(n, l):
    angle = (n - 2) * 180
    if angle % n == 0:
        angle //= n
        for i in range(n):
            tt.forward(l)
            tt.left(180 - angle)


for i in range(3, 15):
    polygon(i, 50)
