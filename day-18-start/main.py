from turtle import Turtle as T, Screen

tim = T()
# You can choose circle or whatever you want
# Check document https://docs.python.org/3/library/turtle.html
tim.shape("turtle")
# Choose any color: red, green, blue, etc.
tim.color("salmon1")
# Moving our turtle
# Let's make  circle
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)

# Easiest way to make a circle is:
for _ in range(4):
    tim.forward(100)
    tim.left(90)
















screen = Screen()
screen.exitonclick()
