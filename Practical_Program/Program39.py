# This python program generates the list in between square of numbers in between n1 amd n2
# And Print the last five numbers from the list 

def main(n1,n2):
    myList = []
    newList = []

    for i in range(n1,n2+1):
        myList.append(i**2)

    # print(myList[-5:])
    for _ in range(5):
        newList.append(myList.pop())

    newList.reverse()
    print(newList)            

if __name__ == "__main__":
    n1 = int(input("Enter the number n1: "))
    n2 = int(input("Enter the number n2: "))

    main(n1,n2)
