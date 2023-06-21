# coding: utf-8

# This python program is using list comprehension and print the list
# after removing the 0th, 2nd, 4th,6th numbers in
# [12,24,35,70,88,120,155].

def main():
    myList = [12,24,35,70,88,120,155] 
    myList = [i for Index,i in enumerate(myList) if Index%2 != 0 ]
    print(myList)

if __name__ == '__main__':
    main()