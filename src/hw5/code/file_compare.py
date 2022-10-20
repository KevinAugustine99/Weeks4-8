"""
File : file_compare.py
Assignment : HW #5
Language : python3
Author : Kevin Augustine < kea4437@rit.edu >
"""
import sys


def char_by_char(file1,file2):
    """char_by_char opens the two text files, reads each line by character, prints out the differences in the two files,the amount of 
    characters in each text file, the amount of unmatched characters, and the amount of times the lines were different lengths.
    file1 = the prompted name for the first text file
    file2 = the prompted name for the second text file
    f1 = the file object variable for the first text file
    f2 = the file object variable for the second text file
    count_line = a counter for which line is being read
    count_char_file1 = a counter for how many characters are in file 1 
    count_char_file2 = a counter for how many characters are in file 2
    count_unmatched_char = a counter for how many times the characters don't match up
    count_different_length = a counter for how many times the lines have different lengths
    line1 = the line from f1
    line2 = the line from f2
    i = a counter for the amount of characters in a line for the loop
    """
    f1 = open(file1)
    f2 = open(file2)

    print("\n","Character by character:", sep='')
    print ("Unmatched characters: ", end='')
    count_line = 0
    count_char_file1 = 0
    count_char_file2 = 0
    count_unmatched_char = 0
    count_different_length = 0
    while True: 
        line1 = f1.readline()
        line2 = f2.readline()
        count_line += 1
        count_char_file1 += len(line1.strip())
        count_char_file2 += len(line2.strip())
        if line1 == "" and line2 == "":
            break

        if len(line1) == len(line2):
            for i in range(len(line1)):

                if line1[i] != line2[i]:
                    count_unmatched_char += 1
                    print(str(count_line),":",str(i+1),", ", sep='', end='')
        else:
            count_different_length += 1
            print(str(count_line), ", ", sep='', end='')
            
    print("\n" , "There are ",str(count_char_file1), " in ", file1, sep='')
    print("There are ",str(count_char_file2), " in ", file2, sep='')
    print("There were ",count_unmatched_char," unmatched characters in the files", sep='')
    print("There were ",count_different_length," lines of different length", sep='')
    f1.close()
    f2.close()


def main():
    # file1 = input("First file name:")
    # file2 = input("Second file name:")

    file1 = "../output.txt"
    file2 = "../given.txt"

    char_by_char(file1,file2)

if __name__ == "__main__":
    main()