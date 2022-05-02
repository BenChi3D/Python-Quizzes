import turtle

shape = turtle.Turtle() #  naming turtle
shape.color("red") #  turtle color

#  lopping over a range of number
for side in range(5):
    shape.forward(2 * side) #  changing with the side number looping
    shape.right(360/side) #  angle change also with side number looping
