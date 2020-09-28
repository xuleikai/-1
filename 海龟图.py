# squarespiral1.py-draw a square spiral
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
sides = eval(input("2-6"))
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
for x in range(720):
     t.pencolor(colors[x%sides])
     t.forward(x*3/sides+x)
     t.left(360/sides+1)
     t.width(x*sides/200)
     t.left(90)
