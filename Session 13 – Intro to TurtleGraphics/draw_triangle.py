import turtle

t = turtle.Turtle()
t.pensize(3)
t.speed(3)

t.color("darkgreen", "lightgreen")
t.begin_fill()

for _ in range(3):
    t.forward(120)
    t.left(120)

t.end_fill()

turtle.done()