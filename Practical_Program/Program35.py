# This python program generate the dictionary where the keys are numbers 
# between 1 and 20(both included) and the values are the square the keys 
# Functions should just print the values of dictionary only
def main(n1,n2):
    dictionary = dict()

    for i in range(n1,n2+1):
        dictionary[i] = pow(i,2)

    print(dictionary.values())        

if __name__ == '__main__':
    n1 = int(input("Enter the n1: "))
    n2 = int(input("Enter the n2: "))
    main(n1,n2)