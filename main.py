from turtle import Turtle, Screen
import random



shape = "circle"
icons = []
max_height=250
max_width=250
total_size = max_height*max_width

# class Turtle(Turtle):
#   def __init__(self,shape,color,x,y):
#     self.shape= shape
#     self.color= color
#     self.x= x
#     self.y= y
    
   

# class Grid:
#   def __init__(self,height,width):
#     self.height= height
#     self.width= width
#   def move(self,turtle,movement,max_height,max_width):
#     turtle.forward(movement)
    
#   def place(self,turtle,max_height,max_width):
#     for y in range(max_height):
#       for x in range(max_width):
#         turtle= Turtle(shape,color,x,y)
#         turtle.setx(x)
#         turtle.sety(y)
#         icons.append(turtle)
 

# grid =Grid(max_height,max_width)
# turtle= Turtle(shape,color,0,0)

# grid.place(turtle,max_height,max_width)

for x in range(-250,max_width,50):
  for y in range(-250,max_height,50):
    color = random.choice(["red", "green", "blue", "yellow", "purple", "orange"])
    timmy= Turtle()
    timmy.penup()
    timmy.shape("circle")
    timmy.color(color)
    timmy.setx(x)
    timmy.sety(y)
screen= Screen()
