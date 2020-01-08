import turtle


def sq(l):
    for i in range(4):
        tt.color(colors[i])
        tt.forward(l)
        tt.left(90)


colors = ['red', 'green', 'blue', 'yellow']

tt = turtle.Turtle()
tt.speed(50)

length = 40
for i in range(50):
    # tt.color(colors[i%2])
    sq(length)
    # tt.circle(length)
    tt.right(8)
    length += 5

