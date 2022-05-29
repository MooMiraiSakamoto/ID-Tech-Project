import turtle
from hero import *

top_edge = 150 # top y coordinate
bottom_edge = -150 # bottom y coordinate
right_edge = 200 # right x coordinate
left_edge = -200 # left x coodinate

t = turtle.Turtle()
t2 = turtle.Turtle()

def draw_grid():
  """
  Draws a big box of grass
  """
  t.color("black", "#90ee90") # "#90ee90" -> light green
  t.begin_fill()
  t.up() # turtle's pen will be up -> turtle will not draw lines
  t.goto(0, 150)
  t.down() # turtle's pen will be down -> it will start drawing lines
  t.goto(-200, 150)
  t.goto(-200, -150)
  t.goto(200, -150)
  t.goto(200, 150)
  t.goto(0, 150)
  t.hideturtle() # turtle's arrow will dissapear
  print(t.filling())
  t.end_fill()
  

def draw_road():
  t.color("#808080") # "#808080" -> gray
  t.pensize(20)
  t.shape("square")
  t.up()
  t.goto(0, 0)
  t.shapesize(stretch_wid = 15, stretch_len = 3.5)
  t.stamp()
  t.goto(50, 150)
  t.pensize()
  t.right(90)
  t.shapesize(stretch_wid = 20, stretch_len = 2) # width --- 400(len of the green square) / 20(pensize)
  t.goto(0, -70)
  t.stamp()
  t.goto(0, 70)
  t.stamp()
  t.ht() # ht -> hide turtle
  t.goto(500, 500)

def draw_rodelines():
  # the position of t2 is (0, 0) at this point
  t2.speed(0) 
  t2.color("YELLOW")
  t2.penup()
  t2.goto(0, 150)
  t2.right(90)
  while t2.ycor() >= -145:
    t2.down()
    t2.forward(5)
    t2.penup()
    t2.forward(5)
  t2.penup()
  t2.goto(-200, 70) # the right side of the top road
  t2.left(90)
  while t2.xcor() <= 195:
    t2.down()
    t2.forward(5)
    t2.penup()
    t2.forward(5)
  t2.penup()
  t2.goto(-200, -70) 
  while t2.xcor() <= 195:
    t2.down()
    t2.forward(5)
    t2.penup()
    t2.forward(5)
  

def main(): # making a function to be called in the main file
  draw_grid()
  draw_road()
  draw_rodelines()
  t2.ht()
  
  # spencer = IceHero("spencer", "S")
  # stephany = FireHero("stephany", "S")
  # hector = Enemy("hector")
  
  # spencer.draw()
  # spencer.ice(hector)
  # hector.draw()
