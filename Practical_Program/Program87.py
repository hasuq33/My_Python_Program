# coding: utf-8

# This python program to print the list after
# removing delete even numbers in [5,6,77,45,22,12,24].


def main():
    myList = [5, 6, 77, 45, 22, 12, 24]
    i = 0
    while i < len(myList):
        if myList[i] % 2 == 0:
            myList.pop(i)
        else:
            i += 1

    print(myList)

if __name__ == "__main__":
    main()
