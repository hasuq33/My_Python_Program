# coding: utf-8

# This python program is use the list comprehension and print the list
# after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].


def main():
    myList = [12,24,35,70,88,120,155]

    myList = [i for Index,i in enumerate(myList) if Index not in (0,4,5)]
    print(myList)

if __name__ == '__main__':
    main()