from turtle import Turtle as T, Screen

tim = T()
# You can choose circle or whatever you want
# Check document https://docs.python.org/3/library/turtle.html
tim.shape("turtle")
# Choose any color: red, green, blue, etc.
tim.color("salmon1")

for _ in range(3):
    tim.forward(50)
    tim.right(120)

tim.color("salmon1")
for _ in range(4):
    tim.forward(50)
    tim.right(90)

tim.color("grey")
for _ in range(5):
    tim.forward(50)
    tim.right(72)

tim.color("black")
for _ in range(6):
    tim.forward(50)
    tim.right(60)

tim.color("blue")
for _ in range(7):
    tim.forward(50)
    tim.right(51.42)

tim.color("yellow")
for _ in range(8):
    tim.forward(50)
    tim.right(45)
















screen = Screen()
screen.exitonclick()
