#The very time consumeing code I spent forever getting to work
import turtle
from turtle import Screen, Turtle
import random as h
import os as o
import time as l
words = ["Strawberry","Eclipse","Chandelier","Ketchup","Toothpaste","Rainbow","Bunkbed","Boardgame","Beehive","Lemon","Wreath","Waffles","Bubble","Whistle","Snowball","Bouquet","Headphones","Fireworks","Igloo","Ferris wheel","Banana peel","Lawnmower","Summer","Whisk","Cupcake","Sleeping bag","Bruise","Fog","Crust","Battery","Paris","Beach","Mountains","Hawaii","Mount Rushmore","USA","Hospital","Attic","Japan","Library","Desert","Mars","Washington DC","Las Vegas","Train station","North Pole","Farm","Disney World","Mexico","Giraffe","Koala","Wasp","Scorpion",'Lion',"Salamander","Dolphin","Frog","Panda","Platypus","T-rex","Meerkat","Eagle","Mailman","Superman","Justin Beiber","Cowboy","Alexander Hamilton","Robin Hood","Vampire","Pirate","Girl Scout","Pikachu","Spongebob","Baby Yoda","Pilgrim","Cinderella","Baker","Abe Lincoln","Thief","Leprechaun","Harry Potter","Shrek","Yoshi","Queen Elizabeth","Cook","Sleep","Plant","Purchase","Tie","Snore","Study","Olympics","Sandcastle","Recycle","Black hole","Applause","Blizzard","Sunburn","Time machine","Monday","Atlantis","Swamp","Panama Canal","Sunscreen","Dictionary","Vanilla","Stapler","Desk","Pay cheque","Work computer","Fax machine","Phone","Paper","Light","Chair","Desk lamp","Notepad","Paper clips","Binder","Calculator ","Calendar ","Sticky Notes ","Pens","Pencils","Notebook","Book","Chairs ","Coffee cup","Coffee mug","Thermos" ,"Hot cup","Glue","Clipboard","Paperclips","Chocolate","Secretary","Work","Paperwork","Workload","Employee","Boredom","Coffee","Golf ","Laptop","Sandcastle","Monday","Vanilla","Bamboo","Sneeze","Scratch ","Celery ","Hammer","Frog ","Tennis","Hot dog","Pants","Bridge","Bubblegum","Candy bar","Bucket","Skiing","Sledding",'Snowboarding','Snowman','Polar bear','Cream','Waffle','Pancakes','Ice cream','Sundae ','beach','Sunglasses','Surfboard','Watermelon','Baseball','Bat','Ball','T-shirt','Kiss','Jellyfish','Jelly','Butterfly','Spider','Broom','Spiderweb','Mummy','Candy','Bays','Squirrels','Basketball','Water Bottle','Unicorn','Dog leash','Newspaper','Hammock','Video camera','Money','Smiley face','Umbrella','Picnic basket','Teddy bear ','Ambulance','Ancient Pyramids','Bacteria','Goosebumps','Pizza','Platypus','Clam Chowder','Goldfish bowl','Skull','Spiderweb','Smoke',"Tree","Ice","Blanket","Seaweed",'Flame','Bubble','Hair','Tooth','Leaf','Worm','Sky','Apple',"Plane",'Cow',"House","Dog","Car","Bed","Furniture","Train","Rainbow","Paintings","Drawing",'Cup',"Plate","Bowl","Cushion","Sofa","Sheet","Kitchen","Table","Candle","Shirt","Clothes","Dress","Pillow","Home","Toothpaste","Guitar","Schoolbag","Pencil Case","Glasses","Towel","Watch","Piano","Pen","Hat","Shoes","Socks","Jeans","Hair Gel","Keyboard","Jacket","Tie","Bandage","Scarf","Hair Brush","Cell Phone"]
choice =h.choice(words)
print(choice)
l.sleep(1.5)
o.system("cls")
print("r:Reset\nw:Increase Size\ns:Decrease Size\n1:Black\n2:White\n3:Increase R in RGB\n4:Increase G in RGB\n5:Increase B in RGB\n6:Decrease R in RGB\n7:Decrease G in RGB\n8:Decrease B in RGB\nUp Arrow: Pick up pen\nDown Arrow: Put pen down")
s = Screen()
t = Turtle("circle")
size = 10
t.pensize(size)
t.speed(0)
SCREEN_WIDTH = 1000
SCREEN_LENGTH = 750
s.setup(SCREEN_WIDTH, SCREEN_LENGTH)
s.title("Pictionary")
r=0
g=0
b=0
t.pd()
s.colormode(255)
# These parameters will be the mouse position
def dragging(x, y): 
  t.ondrag(None)
  t.setheading(t.towards(x, y))
  t.goto(x, y)
  t.ondrag(dragging)
def reset():
  global size
  size = 10
  t.pensize(size)
  t.clear()
  t.color("black")
  t.penup()
  t.goto(0,0)
  t.pendown()
#Varying code for options on turtle drawing
def sizeup():
  global size
  if size <40:
    size +=1
    t.pensize(size)
def sizedown():
  global size
  if size >1:
    size -=1
    t.pensize(size)
# This will run the program
def colorblack():
  t.color("black")
  r=0
  g=0
  b=0
def colorwhite():
  t.color("white")
def colorupred():
  global r, g, b, rgb
  if r <255:
    r += 5
    t.pencolor((r, g, b))
def colorupgreen():
  global r, g, b, rgb
  if g < 255:
    g += 5
    t.pencolor((r, g, b))
def colorupblue():
  global r, g, b, rgb
  if b < 255:
    b += 5
    t.pencolor((r, g, b))
def colordownred():
  global r, g, b, rgb
  if r >0:
    r -= 5
    t.pencolor((r, g, b))
def colordowngreen():
  global r, g, b, rgb
  if g > 0:
    g -= 5
    t.pencolor((r, g, b))
def colordownblue():
  global r, g, b, rgb
  if b >0:
    b -= 5
    t.pencolor((r, g, b))
def penu():
  t.penup()
def pend():
  t.pendown()
def main():
  global a
  turtle.listen()
  t.ondrag(dragging)  # When we drag the turtle object call dragging
  s.onscreenclick(t.goto)
  s.onkeypress(reset, "r")
  s.onkeypress(sizeup, "w")
  s.onkeypress(sizedown, "s")
  s.onkeypress(colorblack, "1")
  s.onkeypress(colorwhite, "2")
  s.onkeypress(colorupred, "3")
  s.onkeypress(colorupgreen, "4")
  s.onkeypress(colorupblue, "5")
  s.onkeypress(penu, "Up")
  s.onkeypress(pend, "Down")
  s.onkeypress(colordownred, "6")
  s.onkeypress(colordowngreen, "7")
  s.onkeypress(colordownblue, "8")
  s.listen()
  t.getscreen().mainloop()  # This will continue running main() 
main()