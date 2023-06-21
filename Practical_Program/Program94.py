# coding: utf-8

# This python program removes all duplicates value from the given list


def main():
    myList = [1,2,3,4,5,6,7,8,9,10,10,9,8,7,6,5,4,3,2,1]
    x = set(myList)
    y = list(x)
    print(y)

if __name__ == "__main__":
    main()