# coding: utf-8

# Shuffle the list in python using random module 

import random

def main(n):
    myList = []
    for i in range(1,n+1):
        myList.append(i)

    random.shuffle(myList)
    print(myList)
    
if __name__ == "__main__":
    n = int(input("Enter the number: "))
    main(n)