# This python program generate the dictionary where the keys are numbers between n1 and
# n2 and the values are square of the keys. And print the keys only

def main(n1,n2):
    dictionary = dict()
    for i in range(n1,n2+1):
        dictionary[i] = pow(i,2)

    print("The dictionary is: ",dictionary)
    print("The dictionary keys are: ",end=" ")
    for i in dictionary.keys():
        print(i,end=" ")
    print()    


if __name__ == "__main__":
    n1 = int(input("Enter the n1: "))
    n2 = int(input("Enter the n2: "))

    main(n1,n2)