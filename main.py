from turtle import Turtle, Screen
import random

# class Turtle(Turtle):
#   def __init__(self,shape,color,x,y):
#     self.shape= shape
#     self.color= color
#     self.x= x
#     self.y= y
    
#   def place(self,x,y):
#     self.x= x
    

class Grid:
  def __init__(self,height,width):
    self.height= height
    self.width= width
    

# max_height= input("Enter the max height of the grid: ")
# max_width = input("Enter the max width of the grid: ")

# grid =Grid(max_height,max_width)

timmy= Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
screen= Screen()
