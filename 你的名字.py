#my name.py
import turtle
t = turtle
turtle.bgcolor("black")
your_name = turtle.textinput("wtf,name","name!!!")
colors = ["red", "blue", "green", "yellow"]
for x in range(100):
     turtle.pencolor(colors[x%4])
     turtle.penup()
     turtle.forward(x*4)
     turtle.pendown()
     turtle.write(your_name, font =("Arial",int( (x+4)/4),"bold"))
     turtle.left(92)
     
