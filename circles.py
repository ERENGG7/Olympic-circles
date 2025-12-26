import turtle
#const for pensize:
PENSIZE = 9

#func for drawing olympic circles:
def olympic_circles():
    it = turtle.Turtle()
    for i in range(3):
        it.penup()
        if i == 0:
            it.goto(-180,0)
            it.color("blue")
        elif i == 1:
            it.goto(-30,0)
            it.color("black")
        else:
            it.goto(120,0)
            it.color("red")
        it.pensize(PENSIZE)
        it.pendown()
        it.circle(60)
        print("star",i+1,"done!")
    for i in range(2):
        it.penup()
        if i == 0:
            it.goto(-105,-60)
            it.color("yellow")
        else:
            it.goto(43,-60)
            it.color("green")
        it.pensize(PENSIZE)
        it.pendown()
        it.circle(60)
        print("star", i + 4, "done!")
    turtle.done()
#circles:    
olympic_circles()