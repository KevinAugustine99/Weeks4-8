"""
File: hw08.py
Author: Kevin Augustine
"""
import time
import random
import merge_sort as m_s
import quick_sort as q_s
import insertion_sort as i_s

def get_list1(n):
    """
    :param n: the length of a list
    :return: a list with random elements (favorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L+[random.random()]
    return L

def get_list2(n):
    """
    :param n: the length of a list
    :return: a list with many repeated elements (favorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L+[random.randint(1,100)]
    return L


def get_list3(n):
    """
    Expected behavior of quick sort: poor
    :param n: the length of a list
    :return: a list of elements increasing overall
    (unfavorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L + [random.random()*i]
    return L

def get_list4(n):
    """
    :param n: the length of a list
    :return: a list with many zeros but neither increasing nor decreasing
    (unfavorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L + [random.randint(-8, 8)*i]
    return L

def merge_quick_sort(lst):
    """merge_quick_sort recursively sorts an unsorted list by spliting the unsorted list into two halves. 
        Then partitions the halves into a less than, same, and greater than lists. The program then recursively
        sorts the less than and greater than lists, after the two halves are sorted, the two halves are merged together.
        lst: the unsorted list
        half1: the first half of the list
        half2: the second half of the list
        less1: all of the values in the first half of the unsorted list that is less than the first value in the half1 list
        same1: all of the values in the first half of the unsorted list that is the same as the first value in the half1 list
        more1: all of the values in the first half of the unsorted list that is more than the first value in the half1 list
        less2: all of the values in the second half of the unsorted list that is less than the first value in the half2 list
        same2: all of the values in the second half of the unsorted list that is the same as the first value in the half2 list
        more2: all of the values in the second half of the unsorted list that is more than the first value in the half2 list
    """
    if lst == []:
        #returns empty list if list is empty
        return []
    elif len(lst) == 1:
        #returns the list if it has a length of one
        return lst
    else:
        #runs if length of the list is greater than one and sorts list, returns sorted list
        ( half1, half2 ) = m_s.split(lst)
        (less1, same1, more1) = q_s.partition(half1[0],half1)
        (less2, same2, more2) = q_s.partition(half2[0],half2)
        return m_s.merge((merge_quick_sort( less1 ) + same1 + merge_quick_sort( more1 )),(merge_quick_sort( less2 ) + same2 + merge_quick_sort( more2 )))
        
def test_merge_quick_sort():
    """test_merge_quick_sort tests the merge_quick_sort function by creating an unsorted list and then sort it using the merge_quick_sort function.
        lst: the unsorted list
    """
    print("Testing the correctness of merge_quick_sort:")
    print("Before sorted:")
    lst = get_list2(20)
    print(lst, end='\n')
    print("After sorted:")
    print(merge_quick_sort(lst))

def print_elapsed_times(lst):
    """test_compare prints the elapsed time for each function one list
        lst: the unsorted list
        func: the function name
        flag: whether the function is insertion_sort or not
        copy: a copy of the list so insertion_sort doesn't modify the original list
        start: the start time before the sort
        end: the end time after the sort
    """
    for (func, flag) in [(i_s.insertion_sort, True) , (m_s.merge_sort, False) , (merge_quick_sort, False) , (q_s.quick_sort, False)]:
        if flag:
            copy = lst[:]
            start = time.time()
            func(copy)
            end = time.time()
            print(func.__name__, "elapsed time:", end-start, "seconds")
        else:
            start = time.time()
            func(lst)
            end = time.time()
            print(func.__name__, "elapsed time:", end-start, "seconds")

def test_compare():
    """test_compare prints the elapsed time for each function for each type of list
    """
    print("\n","Time comparison test begins.","\n","All lists used in this test are of length 10000.","\n", sep='')
    print("Testing with list 1 - random elements")
    print_elapsed_times(get_list1(10000))
    print("\n")
    print("Testing with list 2 - repeated elements")
    print_elapsed_times(get_list2(10000))
    print("\n")
    print("Testing with list 3 - overall increasing elements, not favorable to quick sort")
    print_elapsed_times(get_list3(10000))
    print("\n")
    print("Testing with list 4 - not favorable to quick sort")
    print_elapsed_times(get_list4(10000))
    print("\n")
    print("Time comparison test ends.")

if __name__ == "__main__":
    test_merge_quick_sort()
    test_compare()

