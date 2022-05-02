import turtle

ben = turtle.Turtle()
ben.color("yellow")

def spiral():
    for n in range(101):
        ben.forward(n)
        ben(20)
