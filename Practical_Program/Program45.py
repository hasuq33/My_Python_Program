# This python program filter the even number from the list and return even number list

def even(n):
    if n%2 == 0:
        return n
    

def main(n1,n2):
    myList = []
    for i in range(n1,n2+1):
        myList.append(i) 
    y= filter(even,myList)    
    x = filter(lambda x: x%2==0,myList)  
    print(list(x))     
    print(list(y))



if __name__ == "__main__":
    n1 = int(input("Enter the number n1: "))
    n2 = int(input("Enter the number n2: "))
    main(n1, n2)