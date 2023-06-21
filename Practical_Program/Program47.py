# This python program will filter the even number list and return a square of even number lsits


def main(n1,n2):
    myList = [] 

    for i in range(n1,n2+1):
        myList.append(i)

    x = filter(lambda x:x%2 == 0, myList)
    x = map(lambda x:x**2,x)
    print(list(x))

if __name__ == "__main__":
    n1 = int(input("Enter the number n1: "))
    n2 = int(input("Enter the number n2: "))
    main(n1,n2)