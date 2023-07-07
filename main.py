from turtle import Turtle, Screen
import turtle as t
import random

size=250
t.colormode(255)
timmy= Turtle()
timmy.hideturtle()
timmy.shape("circle")
timmy.speed("fastest")

def random_color():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  color =(r,g,b)
  return color

def draw_grid():
  for y in range(size,-size,-45):
    for x in range(-size,size,45):
      timmy.penup()
      timmy.setx(x)
      timmy.sety(y)
      timmy.pencolor(random_color())
      timmy.color(random_color())
      timmy.stamp()
      
def draw_spirograph():
  for x in range(-size,size,5):
    timmy.pencolor(random_color())
    timmy.penup()
    timmy.setheading(x*3.14)
    timmy.pendown()
    timmy.circle(100)
  

draw_spirograph()
draw_grid()     
screen= Screen()
screen.exitonclick()
