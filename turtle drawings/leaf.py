import turtle

turtle.shape("turtle")
turtle.left(45)
turtle.color("green")
turtle.width(5)



def drawleaf(dist, angle):
    turtle.forward(dist)
    turtle.left(45)
    turtle.forward(dist/2)
    turtle.back(dist/2)
    turtle.right (100)
    turtle.forward(dist/2)
    turtle.back(dist/2)
    turtle.left(55)
    
drawleaf(50, 50)

drawleaf(35, 50)

drawleaf(50, 50)

drawleaf(35, 50)


turtle.exitonclick()
