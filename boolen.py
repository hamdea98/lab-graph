import turtle
t=turtle.Turtle()
def petal(t,r, angle):
    for i in range(2):
        t.circle(r,angle)
        t.left(180-angle)
        
def flower(t, n, angle):
            for i in range(n):
                petal(t, r, angle)
                t.left(360.0/n )
    
def move(t,length):
        window=turtle.Screen()
        window.bgcolor("pink")
        t.pu()
        t.fd(length)
        t.pd()

sam=turtle.Turtle()
sam.speed(8)

sam.color("green")
sam.shape("turtle")
move(sam,-150)
sam.begin_fill()
flower(sam,7,60.0,60.0)
sam.end_fill()
turtle.done()



