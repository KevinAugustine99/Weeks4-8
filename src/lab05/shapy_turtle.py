"""
File : shapy_turtle.py
Assignment : Lab #5
Language : python3
Author : Kevin Augustine < kea4437@rit.edu >
"""
import turtle
import time

def obtain_number(argument:str):
    """obtain_number checks to see if the first character is a digit, reads the next number in the string and returns it.
        If the first character is not a digit, the function returns None.
        If the first character is a digit, the function compiles the number and returns it.
        argument: the string that is being checked for a number
        compile: a compiler of the number from the string
    """
    compile = ""
    if len(argument) == 0:
        return
    elif not argument[0].isdigit():
        return
    else:
        for x in argument:
            if x.isdigit():
                compile = compile + x
            else:
                break
        return int(compile)

def process_two_numbers(argument, a):
    """process_two_numbers returns the numbers for the R, P, and G functions.
        argument: the string that is being processed for the two numbers
        a: the place holder for the string
        number1: the compiler for the first number
        number2: the compiler for the second number
        flag: checks to see if it is compiling the first or second number
    """
    flag = False
    number1 = ""
    number2 = ""
    for w in argument[a+1:]:
        if w.isdigit():
            if not flag:
                number1 = number1 + w
            else:
                number2 = number2 + w
        else:
            if not flag:
                flag = True
            else:
                break
                
    return (int(number1), int(number2))

def error():
    """error prints ERROR and closes the program
    """
    print("ERROR")
    time.sleep(3)
    exit()

def check_error(func_string):
    """check_error checks to see if there is an error
        If there is an error, the program runs the error function.
    """
    a = 0
    if  func_string[-1] == "U" or  func_string[-1] == "D" or func_string[-1].isdigit():
        """Checks to see if the last character is U, D, or is a number.
            If not: runs error function
        """
        pass
    else:
        error()
    
    if func_string[0].isdigit():
        """Checks to see if the first character is a number.
            If so: runs error function
        """
        error()
     
    for x in func_string.strip():
        if not x.isdigit():
            number = obtain_number(func_string[a+1:])

            if x == "<" or x == ">" or x == "S" or x == "T" or x == "C" or x == "F" or x == "B" or x == "R" or x == "P" or x == "G" or x == ",":
                """Checks to see if the character after a <,>,S,T,C,F,B,R,P,G, or ',' symbol is a number.
                    If not: runs error function
                """
                if not number:
                    error()

            elif x == "U" or x == "D":
                """Checks to see if the character after a U or D symbol is a number.
                    If so: runs error function
                """
                if not number:
                    pass
                else:
                    error() 
           
            elif x == "Z":
                """Checks to see if the character after the Z symbol is a number
                    Also checks to see if the number is between 0 and 9
                    If not: runs error function
                """
                if not number:
                    error()
                elif number >= 10 or number < 0:
                    error()
            else:
                """If there is a character that isn't a shapy turtle command or a number: runs error function
                """
                error()

        a += 1            

def string_process(func_string):
    """string_process processes the string and runs the shapy turtle commands
        func_string: the string that the interpretor reads to run the functions
        a: an index for which character the program is in during the string
        number: the number after the nondigit character, could be a number or None
        pre: turtle is in the center, facing east, pen down
        post: all of the shapy turtle functions are run
    """
    a = 0
    for x in func_string:
        if not x.isdigit():
            number = obtain_number(func_string[a+1:])

            if x == "<":
                """Runs the turn left function, maintains the same position
                """
                turtle.lt(number)

            elif x == ">":
                """Runs the turn left function, maintains the same position
                """
                turtle.rt(number)

            elif x == "S":
                """Runs the draw square function, maintains the same position and orientation
                """
                for x in range(4):
                    turtle.lt(90)
                    turtle.fd(number)

            elif x == "T":
                """Runs the draw triangle function, maintains the same position and orientation
                """

                for n in range(3):
                    turtle.lt(120)
                    turtle.fd(number)

            elif x == "C":
                """Runs the draw circle function, maintains the same position and orientation
                """

                turtle.circle(number)

            elif x == "F":
                """Runs the move forward function, maintains the same orientation
                """
                turtle.fd(number)

            elif x == "B":
                """Runs the move backward function, maintains the same orientation
                """

                turtle.bk(number)

            elif x == "U":
                """Runs the penup function, maintains the same position and orientation
                """
                turtle.penup()

            elif x == "D":
                """Runs the pendown function, maintains the same position and orientation
                """
                turtle.pendown()

            elif x == "R":
                """Runs the draw rectangle function, maintains the same position and orientation
                    length: the length of the rectangle
                    width: the width of the rectangle
                """
                (length, width) = process_two_numbers(func_string,a)
                for n in range(2):
                    turtle.lt(90)
                    turtle.fd(length)
                    turtle.lt(90)
                    turtle.fd(width)

            elif x == "P":
                """Runs the draw polygon function, maintains the same position and orientation
                    sides: the amount of sides of the polygon
                    length: how long one side of the polygon is
                """
                (sides, length) = process_two_numbers(func_string, a)
                angle = 180 - (180*(sides-2)/sides)
                print(sides, length, angle)
                for n in range(sides):
                    turtle.lt(angle)
                    turtle.fd(length)

            elif x == "G":
                """Runs the go to function, maintains the same orientation
                """
                (x_cord, y_cord) = process_two_numbers(func_string,a)
                turtle.goto(x_cord,y_cord)

            elif x == "Z":
                """Runs the change color function, maintains the same position and orientation
                """
                if number == 0:
                    turtle.pencolor('red')
                elif number == 1:
                    turtle.pencolor('blue')
                elif number == 2:
                    turtle.pencolor('green')
                elif number == 3:
                    turtle.pencolor('yellow')
                elif number == 4:
                    turtle.pencolor('brown')
                else:
                    turtle.pencolor('black')
 
        a += 1            
        

def main():
    # func_string = input("What would you like to the turtle to do?")
    func_string = "UG100,100DC100UF100D>90P3,50F50T50"
    check_error(func_string)
    string_process(func_string)

    turtle.done()

if __name__ == "__main__":
    main()
 


