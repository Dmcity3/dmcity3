#PythonDraw.py
import turtle
turtle.setup(750,350,200,200)
turtle.penup()
turtle.fd(-350)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("lightcoral")
turtle.seth(-40)
for i in range(5):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2/3)
turtle.done()
