# This python program generate a list of square values of numbers range in between n1 and n2.
# And print the all value from the list except the first five values

def main(n1,n2):
    eList = []
    myList= [] #In this list I will add all elements from the eList except the first five elements
    for i in range(n1,n2+1):
        eList.append(i**2)
    print(eList)   

    for index,value in enumerate(eList):
        if index<5:
            continue
        else:
            myList.append(value)
    
    print(myList)

if __name__ == "__main__":
    n1= int(input("Enter the number n1: "))
    n2= int(input("Enter the number n2: "))
    main(n1, n2)