"""
File : arrow.py
Assignment : Lab #4
Language : python3
Author : Kevin Augustine < kea4437@rit.edu >
"""
import turtle
import math
import random
import time

MAX_FIGURES = 500
BOUNDING_BOX = 200
MAX_DISTANCE = 30
MAX_SIZE = 30
MAX_ANGLE = 30


def draw_triangle(size):
    """draw_ triangle draws one triangle
        size: the random length of the side of the triangle
        red: the random number for the red attribute of the color
        green: the random number for the green attribute of the color
        blue: the random number for the blue attribute of the color

        Pre:
            Turtle is pen up and in the bottom left corner of the triangle. 
        Post:
            Turtle is pen up and in the bottom left corner of the triangle. 
    """
    turtle.colormode(255)
    red = random.randint(10,255)
    green = random.randint(10,255)
    blue = random.randint(10,255)

    turtle.pencolor(red, green, blue)
    turtle.fillcolor(red, green, blue)
    turtle.pendown()
    turtle.begin_fill()

    turtle.fd(size)
    turtle.lt(120)
    turtle.fd(size)
    turtle.lt(120)
    turtle.fd(size)
    turtle.lt(120)

    turtle.end_fill()

    turtle.penup()


def calculate_area(size):
    """calculate_area calculates the area of one triangle and returns it
        size: the random length of the side of the triangle
    """
    return (math.sqrt(3)/4)*(size)**2


def check_boundings(size):
    """check_boundings checks to see if the turtle is going to draw the turtle outside of the bounding box.
       If the triangle can't be drawn then the turtle keeps turning left until the triangle can be drawn.
       size: the random length of the side of the triangle
    """    

    x = turtle.xcor()
    y = turtle.ycor()

    while (((3*size - BOUNDING_BOX )>(x )) or ((BOUNDING_BOX - 3*size)<(x)) or ((-BOUNDING_BOX + 3*size)>(y)) or ((BOUNDING_BOX - 3*size)<(y))):
        turtle.lt( 7 )
        turtle.fd(size*4)
        x = turtle.xcor()
        y = turtle.ycor()
        turtle.bk(size*4)
        

def draw_figures_rec(depth ,acc=0):
    """draw_ triangle draws all of triangles recursively
        size: the random length of the side of triangle
        depth: the amount of triangles to draw
        acc: the accumulator of the area, Pre: acc = 0
        forward: the random distance the turtle moves forward after drawing the triangle.
        angle: the random angle the turtle turns after drawing the triangle
        Pre:
            Turtle is pen up and in the bottom left corner of the first triangle. 
        Post:
            Turtle is pen up and in the bottom left corner of the last triangle. 
    """
    if depth == 0:
        return acc
    else:
        size = random.randint(1,MAX_SIZE)
        check_boundings(size)
        draw_triangle(size)
        forward = random.randint(1,MAX_DISTANCE)
        turtle.fd(forward)
        angle = random.randint(-MAX_ANGLE,MAX_ANGLE)
        turtle.lt(angle)
        acc = acc + calculate_area(size)
        return draw_figures_rec(depth-1,acc)


def draw_figures_iter(depth, acc = 0):
    """draw_ triangle draws all of triangles iteratively
        size: the length of the side of the first triangle
        depth: the amount of triangles to draw
        acc: the accumulator of the area, Pre: acc = 0
        forward: the random distance the turtle moves forward after drawing the triangle.
        angle: the random angle the turtle turns after drawing the triangle
        Pre:
            Turtle is pen up and in the bottom left corner of the first triangle. 
        Post:
            Turtle is pen up and in the bottom left corner of the last triangle. 
    """
    while depth > 0:
        size = random.randint(1,MAX_SIZE)
        check_boundings(size)
        draw_triangle(size)
        forward = random.randint(1,MAX_DISTANCE)
        turtle.fd(forward)
        angle = random.randint(-MAX_ANGLE,MAX_ANGLE)
        turtle.lt(angle)
        acc = acc + calculate_area(size)
        depth = depth - 1
    return acc


def draw_bounding_box():
    """draw_bounding_box draws the bounding box
        x: a counter for the loop
        Pre:
            Turtle is pen up and in the center of the board. 
        Post:
            Turtle is pen up and in the center of the board.
    """
    turtle.bk(BOUNDING_BOX)
    turtle.rt(90)
    turtle.pendown()
    turtle.fd(BOUNDING_BOX)
    x = 0
    while x < 3:
        x = x + 1
        turtle.lt(90)
        turtle.fd(BOUNDING_BOX*2)
    turtle.lt(90)
    turtle.fd(BOUNDING_BOX)
    turtle.lt(90)
    turtle.penup()
    turtle.fd(BOUNDING_BOX)


def main():
    

    depth = int(input("Arrows (0-500): "))
    if 0 <= depth <= MAX_FIGURES:
        
        turtle.speed(0)
        turtle.penup()
        draw_bounding_box()
        print("The area painted is",draw_figures_rec(depth),"units.")
        input("Hit enter to continue...")
        
        turtle.reset()
        
        turtle.speed(0)
        turtle.penup()
        draw_bounding_box()
        print("The area painted is",draw_figures_iter(depth),"units.")
        print("Close the canvas window to quit.")
        turtle.done()
    else:
        print("Arrows must be between 0 and 500 inclusive.")
        time.sleep(2)
        exit()


if __name__ == "__main__":
    main()

