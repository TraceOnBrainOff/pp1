def drawSquare(x,y,n,pen):
    pen.setposition(x,y)
    pen.pendown()
    for i in range(4):
        pen.forward(n)
        pen.right(90)     # Rotate clockwise by 90 degrees
    pen.penup()