#name:Victoria Inahuazo
#email:victoria.inahuazo11@myhunter.cuny.edu
#date: 03/01/24
#the following program generates a blue color and its shades

import turtle

turtle.colormode(255)
tess = turtle.Turtle()
tess.shape("turtle")
tess.backward(100)


#For 0,10,20....250

for i in range (0, 255, 10):
    tess.forward(10)
    tess.pensize(i)
    tess.color(0,0,i)

