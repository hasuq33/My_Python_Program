# coding: utf-8

# This Python program using list comprehension, please write a program
# to print the list after removing delete numbers
# which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

def main():
    myList = [12,24,35,70,88,120,155]
    i=0
    while i<len(myList):

        if myList[i]%5 == 0 and myList[i]%7 == 0:
            myList.pop(i)

        i+=1    

    print(myList)        

if __name__ == "__main__":
    main()