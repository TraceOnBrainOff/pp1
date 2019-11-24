import turtle
maxSize = 40
pen = turtle.Turtle()
def drawSquare(x,y,n):
    pen.setposition(x,y)
    pen.pendown()
    for i in range(4):
        pen.forward(n)
        pen.right(90)     # Rotate clockwise by 90 degrees
    pen.penup()
    

for i in range(4):
    for j in range(4):
        drawSquare(maxSize*i,maxSize*j, 40)

turtle.done()