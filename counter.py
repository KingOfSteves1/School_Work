import turtle
s = turtle.Screen()
num = 0
def add():
  global num
  num += 1
  print(num)
def sub():
  global num
  num-=1
  print(num)
s.onkeypress(add, "Up")
s.onkeyrelease(sub, "Down")
s.listen()
turtle.done()
