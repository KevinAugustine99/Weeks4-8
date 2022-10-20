"""
File : select_median.py
Assignment : Lab #6
Language : python3.7
Author : Kevin Augustine < kea4437@rit.edu >
"""
from time import time

def quick_select(unsorted_list, k):
    """quick_select recursively calls itself until it returns the kth smallest number in an unsorted list of numbers
        unsorted_list: the unsorted list of shop distances
        pivot: the middle element in the list
        smaller_list: all of the elements in the list that are smaller than the pivot
        larger_list: all of the elements in the list that are greater than the pivot
        count: the number of occurrances of the pivot element in the list
        m: the length of the smaller list
    """
    if len(unsorted_list) != 0:
        #runs if the list is not empty
        pivot = unsorted_list[len(unsorted_list)//2]
        smaller_list = []
        larger_list = []
        count = 0
        for x in unsorted_list:
            if x < pivot:
                smaller_list += [x]
            elif x == pivot:
                count += 1
            elif x > pivot:
                larger_list += [x]
        m = len(smaller_list)
        if k >= m and k < (m + count):
            #returns pivot if pivot is the kth smallest value
            return pivot
        elif m > k:
            #recursively calls quick_select if the kth smallest value is less than the pivot
            return quick_select(smaller_list, k)
        else:
            #recursively calls quick_select if the kth smallest value is greater than the pivot
            return quick_select(larger_list, (k-m-count))

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
    text_file = input("Enter data file: ")
    unsorted_list = []

    for line in open(text_file):
        unsorted_list += [int(line.split()[1])]

    if len(unsorted_list) % 2 == 0:
        #calculates median if the list is even
        start_time = time()
        median = (quick_select(unsorted_list,(len(unsorted_list)//2)) + quick_select(unsorted_list,((len(unsorted_list)//2)-1))) / 2
        end_time = time()
    else:
        #calculates median if the list is odd
        start_time = time()
        median = quick_select(unsorted_list,(len(unsorted_list)//2))
        end_time = time()
    print("Optimum new store location: ", median)
    sum_distance = get_sum_distance(unsorted_list,median)
    print("Sum of distances to new store : ", sum_distance)
    print("\n","elapsed time : ", end_time - start_time, sep='')

if __name__ == "__main__":
    main()