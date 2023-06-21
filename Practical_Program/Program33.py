# This python program take an input from user 
# And print the dictionary where the keys are the numbers 1 to n  and the values are the square of the keys

def numDictionary(number):
    dictionary = dict()

    for i in range(1,number+1):
        dictionary[i] = pow(i,2)

    print(dictionary)    

def main():
    number = int(input("Enter the number: "))
    numDictionary(number)

if __name__ == "__main__":
    main()