# coding: utf-8 

# This python program has a binary search function which
# searches an item in a sorted list.
# The function should return
# the index of element to be searched in the list.

import timeit

# Method1 Linear search function
def main(usr,number):
    for Index,i in enumerate(usr):
        if i == number:
            print("Using Linear search Algorithm",Index)

# Method2 Binary Search function
def main1(usr,number):
    endIndex = len(usr) - 1
    startIndex = 0
    Indx = -23
    while endIndex>= startIndex and Indx == -23:
        midValue = int((startIndex + endIndex)/2)

        if usr[midValue] == number:
            print("Using Binary Search Algorithm",midValue)
            break
        elif usr[midValue] > number:
            endIndex = midValue-1
        elif usr[midValue] < number:
            startIndex = midValue+1
        else:
            print("Valure does not exist!")     





if __name__ == "__main__":
    usr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    print(usr)
    number = int(input("Enter which number index do you want to search:"))

    stratTime = timeit.default_timer()
    main(usr,number) #Linear search algorithm
    endtTime = timeit.default_timer()
    Runtime1 = endtTime-stratTime
    print(Runtime1)
    
    startTime1 = timeit.default_timer()
    main1(usr,number)
    endtTime1 = timeit.default_timer()
    print(endtTime1-startTime1)