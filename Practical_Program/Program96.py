# coding: utf-8

# This python program which count and print the numbers of each
# character in a string input by console.

# Example:
# If the following string is given as input to the program:

# abcdefgabc
# Then, the output of the program should be:

# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1

def main(usr):
    myList = []
    for i in usr:
        a= i,",",usr.count(i)
        myList.append(a)

    a = set(myList)
    c=sorted(a)
    for i in c:
        for j in i:
            print(j,end="") 
        print()       
    

if __name__ == "__main__":
    usr = input("Enter some Input: ")
    main(usr)