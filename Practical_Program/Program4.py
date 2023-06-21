# Write a program which accepts comma separated number and returns list and tuple in string format


if __name__ == '__main__':
    numInput = input("Enter the number with comma separated: ")
    list = numInput.split(",")
    tuple = tuple(list)
    print(list) 
    print(tuple)
