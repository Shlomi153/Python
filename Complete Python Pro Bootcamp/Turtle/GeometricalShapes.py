#Created by Shlomi Kiko
#Goal: Display a variety of Geometrical objects one after the other in a Graphical User Interface
#LinkedIn: https://www.linkedin.com/in/shlomikiko/

from turtle import Turtle, Screen

shape_speed = 2
pen_size = 3

##################################################################################################################################
#Triangle
##################################################################################################################################

#Create the Triangle object
triangle_shape = Turtle()
triangle_iterations = 3
triangle_angle = 360 / triangle_iterations
triangle_shape.shape('triangle')


#Set Triangle pen
triangle_shape.pen(fillcolor='DarkSeaGreen1', pencolor='aquamarine', pensize=pen_size, speed=shape_speed)

#Set starting position
triangle_shape.hideturtle()
triangle_shape.penup()
triangle_shape.setpos(50,50)
triangle_shape.showturtle()

#Move the Triangle object
triangle_shape.pendown()

for i in range(triangle_iterations):
    triangle_shape.right(triangle_angle)
    triangle_shape.forward(100)
    
triangle_shape.hideturtle()

##################################################################################################################################
#Square
##################################################################################################################################

#Create the Square object
square_shape = Turtle()
square_iterations = 4
square_angle = 360 / square_iterations
square_shape.shape('square')

#Set Square pen
square_shape.pen(fillcolor='GreenYellow', pencolor='DarkTurquoise', pensize=pen_size, speed=shape_speed)

#Set starting position
square_shape.hideturtle()
square_shape.penup()
square_shape.setpos(triangle_shape.pos())
square_shape.showturtle()

#Move the Square object
square_shape.pendown()

for i in range(square_iterations):
    square_shape.right(square_angle)
    square_shape.forward(100)

square_shape.hideturtle()

##################################################################################################################################
#Pentagon
##################################################################################################################################

#Create the Pentagon object
pentagon_shape = Turtle()
pentagon_iterations = 6
pentagon_angle = 360 / pentagon_iterations
pentagon_shape.shape('circle')

#Set Pentagon pen
pentagon_shape.pen(fillcolor='cyan', pencolor='cyan4', pensize=pen_size, speed=shape_speed)

#Set starting position
pentagon_shape.hideturtle()
pentagon_shape.penup()
pentagon_shape.setpos(square_shape.pos())
pentagon_shape.showturtle()

#Move the Pentagon object
pentagon_shape.pendown()

for i in range(pentagon_iterations):
    pentagon_shape.right(pentagon_angle)
    pentagon_shape.forward(100)

pentagon_shape.hideturtle()

##################################################################################################################################
#Hexagon
##################################################################################################################################

#Create the Hexagon object
hexagon_shape = Turtle()
hexagon_iterations = 8
hexagon_angle = 360 / hexagon_iterations
hexagon_shape.shape('classic')

#Set Hexagon pen
hexagon_shape.pen(fillcolor='CadetBlue3', pencolor= 'CornFlowerBlue', pensize=pen_size, speed=shape_speed)

#Set starting position
hexagon_shape.hideturtle()
hexagon_shape.penup()
hexagon_shape.setpos(pentagon_shape.pos())
hexagon_shape.showturtle()

#Move the Hexagon object
hexagon_shape.pendown()

for i in range(hexagon_iterations):
    hexagon_shape.right(hexagon_angle)
    hexagon_shape.forward(100)

hexagon_shape.hideturtle()

##################################################################################################################################
#Heptagon
##################################################################################################################################

#Create the Heptagon object
heptagon_shape = Turtle()
heptagon_iterations = 9
heptagon_angle = 360 / heptagon_iterations
heptagon_shape.shape('classic')

#Set Heptagon pen
heptagon_shape.pen(fillcolor='bisque', pencolor= 'burlywood4', pensize=pen_size, speed=shape_speed)

#Set starting position
heptagon_shape.hideturtle()
heptagon_shape.penup()
heptagon_shape.setpos(pentagon_shape.pos())
heptagon_shape.showturtle()

#Move the Heptagon object
heptagon_shape.pendown()

for i in range(heptagon_iterations):
    heptagon_shape.right(heptagon_angle)
    heptagon_shape.forward(100)

heptagon_shape.hideturtle()

##################################################################################################################################
#Octagon
##################################################################################################################################

#Create the Octagon object
octagon_shape = Turtle()
octagon_iterations = 10
octagon_angle = 360 / octagon_iterations
octagon_shape.shape('classic')

#Set Octagon pen
octagon_shape.pen(fillcolor='DarkSalmon', pencolor= 'DarkRed', pensize=pen_size, speed=shape_speed)

#Set starting position
octagon_shape.hideturtle()
octagon_shape.penup()
octagon_shape.setpos(pentagon_shape.pos())
octagon_shape.showturtle()

#Move the Octagon object
octagon_shape.pendown()

for i in range(octagon_iterations):
    octagon_shape.right(octagon_angle)
    octagon_shape.forward(100)

octagon_shape.hideturtle()

##################################################################################################################################
#Nonagon
##################################################################################################################################

#Create Nonagon object
nonagon_shape = Turtle()
nonagon_iterations = 11
nonagon_angle = 360 / nonagon_iterations
nonagon_shape.shape('square')

#Set Nonagon pen
nonagon_shape.pen(fillcolor='azure', pencolor='azure3', pensize=pen_size, speed=shape_speed)

#Set starting position
nonagon_shape.hideturtle()
nonagon_shape.penup()
nonagon_shape.setpos(octagon_shape.pos())
nonagon_shape.showturtle()

#Move the Nonagon object
nonagon_shape.pendown()

for i in range(nonagon_iterations):
    nonagon_shape.right(nonagon_angle)
    nonagon_shape.forward(100)

nonagon_shape.hideturtle()

##################################################################################################################################
#Decagon
##################################################################################################################################

#Create the Decagon object
decagon_shape = Turtle()
decagon_iterations = 12
decagon_angle = 360 / decagon_iterations
decagon_shape.shape('turtle')

#Set the pen
decagon_shape.pen(fillcolor='DarkGoldenRod1', pencolor='DarkGoldenRod4', pensize=pen_size, speed=shape_speed)

#Set the starting point
decagon_shape.hideturtle()
decagon_shape.penup()
decagon_shape.setpos(nonagon_shape.pos())
decagon_shape.showturtle()

#Move the Decagon object
decagon_shape.pendown()

for i in range(decagon_iterations):
    decagon_shape.right(decagon_angle)
    decagon_shape.forward(100)

decagon_shape.hideturtle()

screen = Screen()
screen.exitonclick()