# Python program for creating a Tic tac Toe Board using Turtle  
import turtle  
  
# setting a Screen in order to work on it  
sc=turtle.Screen()  
  
# Defining the instance of Turtle  
ttl=turtle.Turtle()  
  
# setting the color of the turtle to color violet  
ttl.color("violet")  
  
# Setting the width of the turtle to 3  
ttl.width("3")  
  
# Setting the speed of drawing to 4  
ttl.speed(4)  
  
# Initialising a for Loop for making the main   
# outline square of length 150  
for j in range(4):  
    ttl.forward(150)  
    ttl.left(90)  
  
  
# The code for making the lines inside the outline square  
ttl.penup()  
ttl.goto(0,50)  
ttl.pendown()  
  
ttl.forward(150)  
  
ttl.penup()  
ttl.goto(0,100)  
ttl.pendown()  
  
ttl.forward(150)  
  
ttl.penup()  
ttl.goto(50,0)  
ttl.pendown()  
  
ttl.left(90)  
ttl.forward(150)  
  
ttl.penup()  
ttl.goto(100,0)  
ttl.pendown()  
  
ttl.forward(150)  
  
ttl.hideturtle()  
