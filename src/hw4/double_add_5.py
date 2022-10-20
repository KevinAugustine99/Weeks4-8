"""
File : double_add_5.py
Assignment : HW #4
Language : python3
Author : Kevin Augustine < kea4437@rit.edu >
"""

def print_sequence_rec( start, count, x=1):
    """print_sequence_rec( start, count ) recursively generates and prints each step
    of the sequence from the start value.
    start: This is where the sequence starts
    count: The amount of steps in the sequence 
    x: checks to see if the function name has been printed yet
    """
    while x==1:
        print("\n","print_sequence_rec( ",start,", ",count,"):",sep='')
        x = 0
    if count == 0:
        print(start, end=" ")
    else:
        print(start, end=" ")
        print_sequence_rec(((2*start)+5),count-1,0)

def print_sequence_iter( start, count, x=1):
    """print_sequence_rec( start, count ) iteratively generates and prints each step
    of the sequence from the start value.
    start: This is where the sequence starts
    count: The amount of steps in the sequence 
    """
    print("\n","print_sequence_iter( ",start,", ",count,"):",sep='')
    while count>=0: 
        print(start, end=" ")
        start = (2*start)+5
        count = count - 1

def find_end_rec( start, count):
    """print_sequence_rec( start, count ) recursively generates and returns the last step
    of the sequence from the start value.
    start: This is where the sequence starts
    count: The amount of steps in the sequence 
    """
    if count == 0:
        return start
    else:
        return find_end_rec(((2*start)+5),count-1)

def find_end_iter( start, count, x=1):
    """print_sequence_rec( start, count ) iteratively generates and returns the last step
    of the sequence from the start value.
    start: This is where the sequence starts
    count: The amount of steps in the sequence 
    """
    while count>0: 
        start = (2*start)+5
        count = count - 1
    return start

def find_start_rec( goal, count, start=0 ):
    """find_start_rec( goal, count ) recursively searches forward from an initial value
    of 0, and returns the smallest integer value that reaches or exceeds the goal.
    start: This is the smallest integer that reaches the goal in count amount of steps, Pre: start = 0
    count: The amount of steps in the sequence
    goal: The expected minimum end of the sequence
    Pre: goal >= 0 and count > 0
    """
    if find_end_iter(start,count) >= goal:
        return start
    else: 
        return find_start_rec(goal, count, start + 1)
def find_start_iter(goal, count, start=0):
    """find_start_iter( goal, count ) iteratively searches forward from an initial value
    of 0, and returns the smallest integer value that reaches or exceeds the goal.
    start: This is the smallest integer that reaches the goal in count amount of steps, Pre: start = 0
    count: The amount of steps in the sequence
    goal: The expected minimum end of the sequence
    Pre: goal >= 0 and count > 0
    """
    while find_end_iter(start,count) < goal:
        start = start + 1
    return start

if __name__ == "__main__":
    print_sequence_rec( 1, 2 )
    print_sequence_rec( 4, 6 )

    print_sequence_iter( 1, 2 )
    print_sequence_iter( 4, 6 ) 

    print("\n","find_end_rec(100,3):","\n",find_end_rec( 100, 3 ) ,sep='')
    print("find_end_rec(200,2):","\n",find_end_rec( 200, 2 ),sep='' )

    print("find_end_iter(100,3):","\n",find_end_iter( 100, 3 ),sep='' )
    print("find_end_iter(200,2):","\n",find_end_iter( 200, 2 ),sep='' )

    print("find_start_rec(500,6):","\n",find_start_rec(500,6),sep='')
    print("find_start_rec(100,3):","\n",find_start_rec(100,3),sep='')

    print("find_start_iter(500,6):","\n",find_start_iter(500,6),sep='')
    print("find_start_iter(100,3):","\n",find_start_iter(100,3),sep='')


