# This python program will 
def main(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return main(n-2) + main(n-1) 
    

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    myList = []
    if n<=0:
        print("Please enter a positive number...")
    else:    
        for i in range(n+1):
            myList.append(main(i))
    # print(myList)

    for Index,i in enumerate(myList): 
        if Index == len(myList)-1:
            print(i,end="")
        else:
            print(i,end=",")    