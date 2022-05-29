import turtle
turtle.addshape("IMG/Enemy.gif")
turtle.addshape("IMG/Enemy Sword.gif")
turtle.addshape("IMG/Fire enemy.gif")
turtle.addshape("IMG/Ice enemy.gif")
turtle.addshape("IMG/Fire hero.gif")
turtle.addshape("IMG/Fire Sword.gif")
turtle.addshape("IMG/Ice hero.gif")
turtle.addshape("IMG/Ice Sword.gif")
class Hero:
  def __init__(self, name, ranking):
    self.name = name
    self.ranking = ranking
  def fly(self):
    print("The hero flies across the city!")
  
class IceHero(Hero):
  def ice(self, enemy):
    enemy.enemy_turtle.shape("IMG/Ice enemy.gif")
    print(f"{enemy.name} has been frozen.")
  def draw(self): # method
    self.hero_turtle = turtle.Turtle() # creates the turtle
    self.hero_turtle.shape("IMG/Ice hero.gif") # shapes the turtle to the "IMG/Ice hero.gif" image
  hero_turtle = turtle.Turtle()
  hero_turtle.shape("IMG/Ice hero.gif")
  hero_turtle.ht()
  
class FireHero(Hero):
  def fire(self, enemy):
    enemy.enemy_turtle.shape("IMG/Fire enemy.gif")
    print(f"{enemy.name} has been burned down into ashes.")
  def draw(self): # method
    self.hero_turtle = turtle.Turtle()
    self.hero_turtle.shape("IMG/Fire hero.gif")  
  hero_turtle = turtle.Turtle()
  hero_turtle.shape("IMG/Fire hero.gif")  
  hero_turtle.ht()
    
class Enemy:
  def __init__(self, name):
    self.name = name
    is_alive = True
    is_frozen = False
    is_burning = False
  def draw(self): # method
    self.enemy_turtle = turtle.Turtle()
    self.enemy_turtle.shape("IMG/Enemy.gif")
  enemy_turtle = turtle.Turtle()
  enemy_turtle.shape("IMG/Enemy.gif")  
  enemy_turtle.ht()