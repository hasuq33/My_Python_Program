
# This python program takes n1 and n2 inputs and pass them in main() function which print the dictionary
# with keys are n1 to n2 numbers and each key has value as the square of key value

def main(n1,n2):
    eDict = dict()
    for i in range(n1,n2+1):
        eDict[i] = pow(i,2);
    print(eDict)



if __name__ == '__main__':
    n1 = int(input("Enter the n1: "))
    n2 = int(input("Enter the n2: "))
    main(n1,n2)