# This python program map the list and give the square of each element value in list

def main(m1,m2):
    myList= []
    for i in range(m1,m2+1):
        myList.append(i)

    x = map(lambda x: x**2 , myList) 
    print(list(x))   


if __name__ == '__main__':
    m1 = int(input("Enter the number m1: "))
    m2 = int(input("Enter the number m2: "))
    main(m1,m2)