import turtle

ts = turtle.Screen()

europa = turtle.Turtle()
africa = turtle.Turtle()
america = turtle.Turtle()
asia = turtle.Turtle()
australia = turtle.Turtle()

for i in [europa, africa, america, asia, australia]:
    i.up()

europa.goto(-100, 100)
africa.goto(0, 100)
america.goto(100, 100)
asia.goto(-50, 50)
australia.goto(50, 50)

for i in [europa, africa, america, asia, australia]:
    i.down()
    i.pensize(4)

europa.color('blue')
africa.color('black')
america.color('red')
asia.color('yellow')
australia.color('green')

for i in [europa, africa, america, asia, australia]:
    i.circle(50)
    i.hideturtle()

ts.mainloop()
