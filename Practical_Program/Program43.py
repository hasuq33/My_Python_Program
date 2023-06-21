# This python program will give even number tuple from given tuple (1,2,3,4,5,6,7,8,9,10)

def main(myTuple):
    myList = list(myTuple)
    evenTuple = []
    for i in myList:
        if i%2 == 0:
            evenTuple.append(i)    
    print(tuple(evenTuple))        

if __name__ == '__main__':
    myTuple = (1,2,3,4,5,6,7,8,9,10)
    main(myTuple)