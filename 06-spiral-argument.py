import turtle

ben = turtle.Turtle()

def spiral(sides, turn, colour, width):
    ben.color(color)
    ben.width(width)
    for side in sides:
        ben.forward(side)
        ben.right(turn)

spiral(100, 50, "green", 5) # a test
