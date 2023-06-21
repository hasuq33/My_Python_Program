# With a given integral number n,
# write a program to generate a dictionary that contains (i, i*i)
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
def myFunc(number):
    myDict = dict() #Initialize empty dictionary
    for i in range(1,number+1):
        myDict[i] = i*i  
    print(myDict,end=" ")      

if __name__ == "__main__":
    number = int(input("Enter the number: "))
    myFunc(number)

#Here we learn to generate a dictionary