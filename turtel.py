from turtle import *
from random import randint

speed(5) #speeds up the turtle
penup()
goto(-140,140) #turtle starts at the center of the screen

for step in range(15):
    write(step,align='center')#align the numbers and the lines
    right(90)
    penup()
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
    
jin=Turtle() #creates new turtle
jin.color('purple')
jin.shape('turtle')

jin.penup()
jin.goto(-160,100) #goes to starting line
jin.pendown()

for turn in range(10):
    jin.right(36)

suga=Turtle() #creates new turtle
suga.color('teal')
suga.shape('turtle')

suga.penup()
suga.goto(-160,75) #goes to starting line
suga.pendown()

suga.right(360)

tae=Turtle() #creates new turtle
tae.color('orange')
tae.shape('turtle')

tae.penup()
tae.goto(-160,50) #goes to starting line
tae.pendown()
tae.left(360)

rm=Turtle() #creates new turtle
rm.color('green')
rm.shape('turtle')

rm.penup()
rm.goto(-160,25) #goes to starting line
rm.pendown()

for turn in range(5):
    rm.left(72)

jk=Turtle() #creates new turtle
jk.color('red')
jk.shape('turtle')

jk.penup()
jk.goto(-160,0) #goes to starting line
jk.pendown()

jk.right(360)

for turn in range(100):
    jin.forward(randint(1,5))
    suga.forward(randint(1,5))
    tae.forward(randint(1,5))
    rm.forward(randint(1,5))
    jk.forward(randint(1,5))
    


