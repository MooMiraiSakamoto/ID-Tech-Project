"""
Author: Mirai Sakamoto
Last updated: 5/29/2022
Purpose: To practice classes and inheritance.
"""

from hero import *
from turtle_game import main
import tkinter as tk
VAL = 100 # one side of a square in the back ground is 100
root = tk.Tk()
root.title("Super hero game")

def create_ice_hero():
  character = IceHero("Jim", "S")
  character.hero_turtle.st() # showing the hero turtle
  play(character)
def create_fire_hero():
  character = FireHero("John", "S")
  character.hero_turtle.st()
  play(character)
  
def character_up(character):
  character.hero_turtle.goto(character.hero_turtle.position()[0], character.hero_turtle.position()[1] + VAL) # the bracket is accessing the index of the coordinates
def character_down(character):
  character.hero_turtle.goto(character.hero_turtle.position()[0], character.hero_turtle.position()[1] - VAL) # the bracket is accessing the index of the coordinates
def character_right(character):
  character.hero_turtle.goto(character.hero_turtle.position()[0] + VAL, character.hero_turtle.position()[1]) # the bracket is accessing the index of the coordinates
def character_left(character):
  character.hero_turtle.goto(character.hero_turtle.position()[0] - VAL, character.hero_turtle.position()[1]) # the bracket is accessing the index of the coordinates
def fight():
  print("BATTLE!!!!!")
def play(character):
  """
  This is the main game loop.
  """
  root.withdraw() # hide the window
  main()
  character.draw()
  character.hero_turtle.penup()
  character.hero_turtle.goto(-150, 100)
  enemy = Enemy("hector")
  enemy.draw()
  enemy.enemy_turtle.penup()
  enemy.enemy_turtle.goto(50, 0)
  enemy.enemy_turtle.st() # st -> show turtle
  print(character.name)
  window = turtle.Screen() #find the window
  window.tracer = 0 # speeds up the turtle animation
  game_state = True
  while game_state == True:
    window.update() # update the turtle screen with current data
    window.listen() # listen for the different key pressed
    window.onkeypress(lambda: character_up(character), "Up")
    window.onkeypress(lambda: character_down(character), "Down")
    window.onkeypress(lambda: character_left(character), "Left")
    window.onkeypress(lambda: character_right(character), "Right")
    if (character.hero_turtle.position()[0] == 
      enemy.enemy_turtle.position()[0] and 
      character.hero_turtle.position()[1] == 
      enemy.enemy_turtle.position()[1]):
      fight()
  
tk.Label(master = root, text = "Choose a character to become: ").pack()
ice_btn = tk.Button(master = root, text = "ice hero", command = create_ice_hero)
fire_btn = tk.Button(master = root, text = "fire hero", command = create_fire_hero)

ice_btn.pack()
fire_btn.pack()

root.mainloop()
