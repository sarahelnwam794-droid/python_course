import turtle

t = turtle.Turtle()
t.speed(5)

t.color("gold", "yellow")

t.begin_fill()
for _ in range(5):
    t.forward(120)
    t.right(144)
t.end_fill()

turtle.done()