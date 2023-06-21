# This python program use generator for give the value of even number
# in between 0 to n.                                             
def main(n):
    myList = []
    def gen(n):
         yield n
        
    for i in range(n+1):
        g = gen(i)
        value = g.__next__() 
        if value%2 == 0:
            myList.append(value)
    
    return myList


if __name__ == "__main__":
    n = int(input("Enter the number: "))
    l= main(n)
    for Index,i in enumerate(l):
        if Index == len(l)-1:
            print(i,end="")
        else:
            print(i,end=",")    
