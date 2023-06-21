# This python program gives us random even number output between 1 to 100
import random

def main():
    myList = []
    for i in range(10):
        n = random.randint(1,10)
        if n%2 == 0:
            myList.append(n)

    a = set(myList)
    for i in a:
        print(i,end=" ")      


if __name__ == "__main__":
    main()