import turtle
import math

if __name__ == '__main__':
    length, eachAngle = 300, 36
    offset = (length / 2) * math.tan((math.pi * eachAngle) / 180) * 1 / 2

    turtle.color('white')
    turtle.setpos(-length / 2, offset)
    turtle.color('cyan', 'cyan')

    turtle.begin_fill()
    for i in range(5):
        turtle.fd(length)
        turtle.right(180 - eachAngle)
    turtle.end_fill()
    turtle.hideturtle()
    turtle.done()
