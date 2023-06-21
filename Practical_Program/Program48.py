# This python program filter a list whose elements are between 1 and 20 and returns a even number list

def main(m1,m2):
    myList = []
    for i in range(m1,m2+1):
        myList.append(i)

    x = filter(lambda x: x%2==0 , myList)
    print(list(x))    

if __name__ == '__main__':
    m1 = int(input("Enter the number m1: "))
    m2 = int(input("Enter the number m2: "))
    main(m1,m2)