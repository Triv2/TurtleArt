from turtle import Turtle, Screen
import turtle as t
import random


max_height=250
max_width=250


# class Turtle(Turtle):
#   def __init__(self,shape,color):
#     self.shape= shape
#     self.color= color
    
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

t.colormode(255)
timmy= Turtle()
timmy.penup()
timmy.hideturtle()
timmy.shape("circle")
timmy.speed("fastest")

def random_color():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  color =(r,g,b)
  return color

def draw_grid(max_height,max_width):
  for y in range(max_height,-max_height,-50):
    for x in range(-max_width,max_width,50):
      timmy.setx(x)
      timmy.sety(y)
      timmy.pencolor(random_color())
      timmy.color(random_color())
      timmy.stamp()
      
def draw_spirograph():
  for x in range(-100,100,2):
    timmy.pencolor(random_color())
    timmy.penup()
    timmy.setheading(x*3.14)
    timmy.pendown()
    timmy.circle(100)
  

draw_spirograph()
# draw_grid(max_height,max_width)     
screen= Screen()
