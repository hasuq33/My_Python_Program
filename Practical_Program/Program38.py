# This Python program which can generate a list in between input number n1 and  n2
# and gives the values are squares 
# And print the first element five elements of the list 

# Method 1 without using slicing 
# def main(n1,n2):

#     list1 = []
#     list2 = []
#     for i in range(n1,n2+1):
#         list1.append(i**2)
    
#     print("Our original list :",list1)
#     for index,i in enumerate(list1):    
#         if index == 5:
#             break
#         else:
#             list2.append(i)
#     s1 = enumerate(list2)
#     print(list(enumerate(list2)))
#     print("First five element of List",list2)        

# Method 2 with using slicing
def main(n1,n2):    
    myList = []

    for i in range(n1,n2+1):
        myList.append(i**2)
    print(myList)   
    newList = myList[:5] 
    print(newList)

if __name__ == '__main__':
    n1 = int(input("Enter the number n1: "))
    n2 = int(input("Enter the number n2: "))
    main(n1,n2)