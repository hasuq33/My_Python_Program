# Write a program that accepts a sequence of whitespace separated words as
# input and prints the words after removing all duplicate words and
# sorting them alphanumerically.

# Suppose the following input is supplied to the
# program:
# hello world and practice makes perfect and hello world again

# Then, the output should be:
# again and hello makes perfect practice world

def main():
    usr = input("Enter the text: ")
    list = usr.split(" ")
    list.sort()
    tuple_list = tuple(list)
    for i in tuple_list:
        print(i,end=" ")
    print()        
    

if __name__ == '__main__':
    main()