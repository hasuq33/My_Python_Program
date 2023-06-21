# This python program will generate a tuple in between number n1 and n2

def main(n1,n2):
    myList=[]
    for i in range(n1,n2+1):
        myList.append(i)

    print(tuple(myList))     

if __name__ == "__main__":
    n1 = int(input("Enter the number n1: "))
    n2 = int(input("Enter the number n2: "))
    main(n1,n2)