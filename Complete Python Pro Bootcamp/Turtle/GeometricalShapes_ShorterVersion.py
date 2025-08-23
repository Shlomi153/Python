#Created by Shlomi Kiko
#Goal: Display a variety of Geometrical objects one after the other in a Graphical User Interface
#LinkedIn: https://www.linkedin.com/in/shlomikiko/

#Plan:
#Make a function to handle the number of iterations
#Make a function to use the first function and define properties
#Make a list of colors and a list of shapes to be used with a random element
#Loop over these shapes and consider the number of angles as iterations:
#Triangle, Square, Pentagon, Hexagon, Heptagon, Octagon, Nonagon, Decagon
#Important to note, the angles need to be of float values to correctly calculate the turns

#Import the required libraries
from turtle import Turtle, Screen
import random as rand

#Function that moves the object and causes it to turn
def move_object(corners, angle):
    for corner in range(corners):
        geometric_shape.forward(100)
        geometric_shape.right(angle)

#Function that calculates the angle
def turn_angle(corners):
    circle = 360
    angle = circle / corners
    return angle

#Function that sets the starting position
def starting_position():
    geometric_shape.penup()
    geometric_shape.setpos(-50,85)
    geometric_shape.pendown()

#Lists and variables to be used
colors = ['red', 'green', 'blue', 'cyan', 'lightgreen', 'turquoise', 'skyblue']
shapes = ['circle', 'triangle', 'classic', 'turtle', 'square']
sizes = [1 , 2, 3]
speed = 1

#Create the Geometrical object
geometric_shape = Turtle()

#Loop n number of times for all desired geometrical objects, Decagon is the last, Triangle is the first, Decagon has 10 corners, Triangle 3
for corners in range(3, 11):
    geometric_shape.pen(fillcolor=rand.choice(colors), pencolor=rand.choice(colors), pensize=rand.choice(sizes), speed=speed)
    geometric_shape.shape(rand.choice(shapes))
    
    starting_position()
    angle = turn_angle(corners)
    move_object(corners, angle)

geometric_shape.hideturtle()

#Keep the screen open until closed manually
screen = Screen()
screen.exitonclick()



    


