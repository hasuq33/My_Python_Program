# This python program converts the all value in the list in square value using map()

def main(n1,n2):
    myList = []
    for i in range(n1,n2+1):
        myList.append(i)
    x = map(lambda x: x**2, myList)    
    print(list(x))

if __name__ == "__main__":
    n1 = int(input("Enter the number n1: "))
    n2 = int(input("Enter the number n2: "))
    main(n1,n2)