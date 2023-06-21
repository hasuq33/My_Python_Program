# This python program generates random numbers output which is divisible by 5 and 7

import random

def main(n1,n2):
    myList = []
    for i in range(n1,n2+1):
        n = random.randint(n1,n2)
        if n%5==0 and n%7 == 0:
            myList.append(n)

    x = set(myList)

    for i in x:
        print(i,end=" ") 
        
if __name__ == "__main__":
    n1 = int(input("Enter the number n1: "))
    n2 = int(input("Enter the number n2:"))
    main(n1,n2)