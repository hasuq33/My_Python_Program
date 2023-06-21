# This python program will show you 'Yes' when you Enter "Yes" , "yes" or "YES" otherwise it 
# will print 'No'

def main():
    while True:
        usr = input("Enter som input: ")

        if usr == "yes" or usr == "Yes" or usr == "YES":
            print("Yes")
        elif usr == "":
            break    
        else:
            print("No")    

if __name__ == "__main__":
    main()