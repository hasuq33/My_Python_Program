# coding: utf-8

# This python program remove 24 value from the list [12,24,35,24,88,120,155]
# after that it prints the list 

def main():
    myList = [12,24,35,24,88,120,155]
    myList = [ i for i in myList if i!= 24]
    print(myList)

if __name__ == '__main__':
    main()