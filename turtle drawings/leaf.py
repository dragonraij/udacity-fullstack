import turtle
import time

turtle.shape("turtle")
turtle.bgcolor("#4DB8FF")
turtle.left(90)
time.sleep(5)


def drawGround(dist):
    turtle.left(90)
    turtle.width(100)
    turtle.color("#663300")
    turtle.forward(dist)
    turtle.back(dist*2)
    turtle.forward(dist)
    turtle.width(3)
    turtle.color("green")
    turtle.right(90)
    turtle.setx(dist)
    for x in range(0, 40):
        turtle.right(45)
        turtle.forward(100)
        turtle.back(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.back(100)
        turtle.left(45)
        turtle.forward(20)
        turtle.right(90)
def drawStem(dist):
    turtle.width(7)
    turtle.color("#006B00")
    turtle.forward(dist)
    
def drawleaf(dist, angle):
    turtle.width(5)
    turtle.color("#006B00")
    turtle.left(angle)
    turtle.forward(dist)
    turtle.color("#5C8533", "#669900")
    turtle.begin_fill()
    turtle.left(45)
    turtle.width(2)
    turtle.forward(dist)
    turtle.right(20)
    turtle.forward(dist/2)
    turtle.right(20)
    turtle.forward(dist/2)
    turtle.right(30)
    turtle.forward(dist)
    turtle.right(100)
    turtle.forward(dist)
    turtle.right(20)
    turtle.forward(dist/2)
    turtle.right(20)
    turtle.forward(dist/2)
    turtle.right(20)
    turtle.forward(dist/2)
    turtle.right(25)
    turtle.forward(dist/2)
    turtle.right(25)
    turtle.forward(dist/2)
    turtle.end_fill()
    turtle.width(3)
    turtle.color("#006B00")
    turtle.right(125)
    turtle.forward(dist)
    turtle.width(2)
    turtle.left(45)
    turtle.forward(dist/2)
    turtle.back(dist/2)
    turtle.right(90)
    turtle.forward(dist/2)
    turtle.back(dist/2)
    turtle.left(45)
    turtle.back(dist*1.9)
    turtle.right(angle)
    turtle.hideturtle()

def drawFlower(dist):
    for x in range(0, 25):
        turtle.begin_fill()
        turtle.width(3)
        turtle.color("orange", "pink")
        turtle.right(15)
        turtle.forward(dist)
        turtle.left(45)
        turtle.forward(dist/2)
        turtle.left(120)
        turtle.forward(dist/2)
        turtle.left(45)
        turtle.forward(dist)
        turtle.end_fill()
    turtle.color("#CCCC00", "#FFFF66")
    turtle.begin_fill()
    turtle.penup()
    turtle.forward(40)
    turtle.pendown()
    
    turtle.left(90)
    turtle.circle(40)
    turtle.end_fill()
    #turtle.left(90)
    #turtle.circle(50,120)
    #turtle.right(90)
    #turtle.circle(50,120)


turtle.sety(-250)
drawGround(400)
turtle.setx(0)
drawStem(100)    
drawleaf(30, -50)
drawleaf(30, 50)
drawStem(50)    
drawleaf(30, 50)
drawStem(50)
drawleaf(30, -50)
drawStem(150)    
drawFlower(75)
turtle.exitonclick()
