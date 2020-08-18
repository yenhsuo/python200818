import turtle
a = turtle.Turtle()
b = turtle.Turtle()
a.color('green')
b.color('blue')
a.pensize(5)
b.pensize(5)
for i in range(360):
    a.forward(1)
    b.forward(1)
    a.left(1)
    b.right(1)
