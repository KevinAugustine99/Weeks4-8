"""
File : store_location.py
Assignment : Lab #6
Language : python3.7
Author : Kevin Augustine < kea4437@rit.edu >
Author of quick_sort and partition: Arthur Nunes-Harwitt, Ivona Bezakova
"""
from time import time

def quick_sort( L ):
    """
    quickSort: List( A ) -> List( A )
        where A is 'totally ordered'
    """
    if L == []:
        return []
    else:
        pivot = L[0]
        ( less, same, more ) = partition( pivot, L )
        return quick_sort( less ) + same + quick_sort( more )

def partition( pivot, L ):
    """
    partition: A * List( A ) -> Tuple( List( A ), List( A ), List( A ) )
        where A is totally ordered
    """
    ( less, same, more ) = ( [], [], [] )
    for e in L:
        if e < pivot:
            less.append( e )
        elif e > pivot:
            more.append( e )
        else:
            same.append( e )
    return ( less, same, more )

def get_median(unsorted_list):
    """get_median sorts the list and then returns the median of the list
        unsorted_list: the unsorted list of store distances
        median: the median of the store distances (location of the donut shop)
        sorted_list: the sorted list of store distances
    """
    median = 0
    sorted_lst = quick_sort(unsorted_list)
    if len(sorted_lst) % 2 == 0:
        # finds the median if the length of the list is even
        median = (sorted_lst[len(sorted_lst)//2]+ sorted_lst[(len(sorted_lst)//2)-1])/2
    else:
        # finds the median if the length of the list is odd
        median = sorted_lst[len(sorted_lst)//2]
    return median

def get_sum_distance(unsorted_list,median):
    """get_sum_distance calculates and returns the total distance from all of the buildings to the donut shop
        unsorted_list: the unsorted list of store distances
        median: the median of the store distances (location of donut shop)
        sum: the total distance from all of the buildings to the donut shop
    """
    sum = 0
    for x in unsorted_list:
        sum += abs(median-x)
    return sum

def main():
    # text_file = input("Enter data file: ")
    text_file = "k.txt"
    unsorted_list = []
    for line in open(text_file):
        unsorted_list += [int(line.split()[1])]

    start_time = time()
    median = get_median(unsorted_list)
    end_time = time()
    print("Optimum new store location: ", median)
    sum_distance = get_sum_distance(unsorted_list,median)
    print("Sum of distances to new store : ", sum_distance)
    print("\n","elapsed time : ", end_time - start_time, sep='')

if __name__ == "__main__":
    main()