from turtle import Turtle as T, Screen
import random

tim = T()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
"LightSeaGreen", "wheat", "SlateGrey", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)


