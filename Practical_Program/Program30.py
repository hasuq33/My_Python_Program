# Define a function that can accept two strings
# as input and concatenate them and then print it in console.

def main(usr1,usr2):
    print(usr1+usr2)

if __name__ == '__main__':
    usr1 = input("Enter first string: ")
    usr2 = input("Enter second string: ")

    main(usr1,usr2)