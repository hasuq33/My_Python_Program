# This python program has a tuple (1,2,3,4,5,6,7,8,9,10) 
# This program prints the first half elements in one line and the second half in another line

def main(n1):
    fList = []
    sList = []

    for index,value in enumerate(n1):
        if index<len(n1)/2:
            fList.append(value)
        else:
            sList.append(value)    
    
    for index,i in enumerate(fList):
        if index == len(fList)-1:
            print(i,end=" ")
        else:
            print(i,end=",")    
    print()    
    for index,i in enumerate(sList):
        if index == len(sList)-1:
            print(i,end=" ")
        else:
            print(i,end=",")    
    print()    

if __name__ == "__main__":
    n1=(1,2,3,4,5,6,7,8,9,10)
    main(n1)