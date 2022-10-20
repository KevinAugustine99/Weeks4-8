"""
File : selection_sort.py
Assignment : HW #7
Language : python3
Author : Kevin Augustine < kea4437@rit.edu >

1. In what kind of test case does insertion_sort perform better than selection_sort?
Clearly describe the test case.

For very very large lists, insertion_sort performs much better, because it only searches through the already sorted section of the list.
Test case: very large lists

2. Why does selection_sort perform worse than insertion_sort in that test case?

selection_sort searches through every unsortedvalue in the table picks the smallest value, and flips it with the mark,
whereas insertion_sort only compares the mark to the number before it. The selection_sort searches through more numbers than the insertion_sort.

"""
def find_min_from(unsorted_list, idx):
    """
    find_min_from checks the unsorted section of the unsorted list and returns the index of the smallest number
    unsorted_list: the unsorted list
    idx: the index of the mark
    best_min: the index of the smallest number in the unsorted section of the list
    number: the index for each value in the unsorted section of the list
    """
    best_min = idx
    for number in range (idx, len(unsorted_list)):
        """checks each value in unsorted section of the list
        """
        if unsorted_list[number]< unsorted_list[best_min]:
            """checks to see if the current value is less than the smallest value
            """
            best_min = number
    return best_min

def selection_sort(unsorted_list):
    """
    selection_sort sorts through the unsorted list and returns the sorted list
    unsorted_list: the unsorted list
    idx: the index/mark from the unsorted list
    min_idx: the index of the smallest number in the unsorted section of the list
    temporary: a temporary placeholder for the value in the mark
    """
    
    for idx in range (len(unsorted_list)):
        min_idx = find_min_from(unsorted_list,idx)
        temporary = unsorted_list[idx]
        unsorted_list[idx] = unsorted_list[min_idx]
        unsorted_list[min_idx] = temporary
    return unsorted_list

def main():
    """
    main opens an inputed text file, reads the lines to make a list,
    prints the unsorted list, sorts the list and prints the sorted list.
    text_file: the name of text file
    file1: the file that was opened
    unsorted_list: the unsorted list from the text file
    sorted_list: the sorted list
    """
    # text_file = input("Which file would you like sorted?")
    text_file = "list.txt"
    file1 = open(text_file)
    unsorted_list = []
    for line in file1:
        unsorted_list += [int(line.strip())]
    file1.close()
    print("\n","Unsorted List: ",unsorted_list, sep="")
    sorted_list = selection_sort(unsorted_list)
    print("\n","Sorted List:", sorted_list, sep="")
    
if __name__ == "__main__":
    main()