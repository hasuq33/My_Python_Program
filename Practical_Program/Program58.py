# This python program is takes an input as a 'username@companyname.com' format 
# And gives the username from the email address 
def main(n1):
    myList = []
    for i in n1:
        if i == '@':
            break
        else:
            myList.append(i)
    print("The user name is : ",end="")          
    for i in myList:
        print(i,end="") 
    print()       

if __name__ == "__main__":
    n1 = input("Enter your email in the 'username@companyname.com' format: ")
    main(n1)