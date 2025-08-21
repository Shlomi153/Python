#Created by Shlomi Kiko
#Goal: Display a variety of Geometrical objects one after the other in a Graphical User Interface
#LinkedIn: https://www.linkedin.com/in/shlomikiko/


#Plan:
#Make a function to handle the number of iterations
#Make a functions to use the first function and define properties
#Make a list of colors and a list of shapes to be used with a random element

import random as rand
from turtle import Turtle, Screen

def move_object(corners):
    circle = 360
    angles = int(circle / corners)

    for i in range(corners):
        geometric_shape.right(angles)
        geometric_shape.forward(100)
      

colors = ['red', 'green', 'blue', 'cyan', 'lightgreen', 'turquoise', 'skyblue']
shapes = ['circle', 'triangle', 'classic', 'turtle']
size = [1, 2, 3, 4]

geometric_shape = Turtle()

for i in range(3, 11):
    geometric_shape.shape(rand.choice(shapes))
    geometric_shape.pen(fillcolor=rand.choice(colors), pencolor=rand.choice(colors), pensize=rand.choice(size), speed=2)

    move_object(i)

geometric_shape.hideturtle()

screen = Screen()
screen.exitonclick()




    


