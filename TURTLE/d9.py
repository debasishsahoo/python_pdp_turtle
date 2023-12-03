#Python program to create a simple animation using turtle  
# importing the reqd modules  
from turtle import *  
from random import randint  
  
      
# Original turtle shaped  
speed(0.1)  
penup()  
goto(-140, 140)  
  
# Drawing the race track  
  
for j in range(15):  
    write(j, align ='center')  
    right(90)  
      
    for num in range(8):  
        penup()  
        forward(10)  
        pendown()  
        forward(10)  
          
    penup()  
    backward(160)  
    left(90)  
    forward(20)  
  
# details of the first player  
plyr1 = Turtle()  
plyr1.color('magenta')  
plyr1.shape('turtle')  
  
# Proceedings of the first player to the race track  
plyr1.penup()  
plyr1.goto(-160, 100)  
plyr1.pendown()  
  
# Turning 360 degrees on the spot  
for turn in range(10):  
    plyr1.right(36)  
  
# details of the second player  
plyr2 = Turtle()  
plyr2.color('red')  
plyr2.shape('turtle')  
  
# Proceedings of the second player to the race track  
plyr2.penup()  
plyr2.goto(-160, 70)  
plyr2.pendown()  
  
# Turning 360 degrees on the spot  
for turn in range(72):  
    plyr2.left(5)  
  
# details of the third player  
plyr3 = Turtle()  
plyr3.shape('turtle')  
plyr3.color('light green')  
  
# Proceedings of the third player to the race track  
plyr3.penup()  
plyr3.goto(-160, 40)  
plyr3.pendown()  
  
# Turning 360 degrees on the spot  
for turn in range(60):  
    plyr3.right(6)  
  
# details of the fourth player  
plyr4 = Turtle()  
plyr4.shape('turtle')  
plyr4.color('blue')  
  
# Proceedings of the third player to the race track  
plyr4.penup()  
plyr4.goto(-160, 10)  
plyr4.pendown()  
  
# Turning 360 degrees on the spot  
for turn in range(30):  
    plyr4.left(12)  
  
# turtles running at random speeds  
for turn in range(100):  
    plyr1.forward(randint(1, 5))  
    plyr2.forward(randint(1, 5))  
    plyr3.forward(randint(1, 5))  
    plyr4.forward(randint(1, 5))  