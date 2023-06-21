# define the function which accepts the two strings as input and  compare two input's 
# lengths and returns maximum length input.
# If length of two inputs are same then it will print both input line by line

def acceptString(usr1,usr2):
    if len(usr1) > len(usr2):
        print(usr1)
    elif len(usr2)<len(usr1):
        print(usr2)
    elif len(usr1)== len(usr2):
        print(usr1)
        print(usr2)
    else:
        print("Kyu Hila dala na")         

def main():
    usr1 = input("Enter the text1: ")
    usr2 = input("Enter the text2: ")

    acceptString(usr1,usr2)

    

if __name__ == '__main__':
    main()