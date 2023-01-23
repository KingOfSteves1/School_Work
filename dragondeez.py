#importing turtle

import turtle

t= turtle.Turtle()

turtle.Screen().bgcolor("light blue")

t.turtlesize(.005)

t.pensize(10)

t.speed(1000)

because=0

#Body

while because<1:

    t.color("pink")
    
    t.begin_fill()
    
    t.left(90)
    
    h=0
    
    while h<60:
        
        t.forward(6)
        
        t.right(3)
        
        h+=1
        
        #tail
        
    t.left(87)

    lt=0
    
    while lt < 100:
        
        t.forward(3)
        
        t.right(.5)
        
        lt+=2.5
        
        #bottom Side

    t.left(203)
    
    t.forward(350)

        #head
    
    h=0
    
    l=0
    
    while h<20:
        
        t.forward(3)
        
        t.right(h)
        
        h+=1
        
        because+=1
        
        if h==19:
            
            t.left(5)
            
            t.forward(10)
            
            t.end_fill()
        
#eyes

t.goto(-10,0)

t.color("black")

t.forward(.1)        

t.color("pink")

t.pensize(.001)

t.goto(90,50)

t.color("black")

t.pensize(10)

t.right(100)

t.forward(30)

t.right(90)

t.forward(30)

while True:

    t=0
    
    t+=1
