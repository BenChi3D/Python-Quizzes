import turtle

ben = turtle.Turtle() # naming turtle
ben.color("cyan") # turtle color

# spirangle code
for side in range(20):
    ben.forward(10 * side)
    ben.right(120)
