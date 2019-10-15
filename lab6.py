#Caitlin De Vita
#caitlin.devita1@marist.edu
#Creating a Traffic Light with Functions

from graphics import *

win= GraphWin("Traffic_light", 200, 200)

def draw_light_body(x, y, length, width):
    body=Rectangle (Point(x,y), Point(length, width))
    body.setFill("white")
    body.setOutline("black")
    body.draw(win)

def draw_lamp(color, a, b, radius):
    lamp = Circle(Point(a,b), radius)
    lamp.setFill(color)
    lamp.setOutline("black")
    lamp.setWidth(3)
    lamp.draw(win)

def draw_traffic_light(x, y):
    draw_light_body(x,y,75, 155)
    draw_lamp("red", 50,30,10)
    draw_lamp("yellow", 50,80,10)
    draw_lamp("green", 50, 130, 10)

draw_traffic_light(25,5)
