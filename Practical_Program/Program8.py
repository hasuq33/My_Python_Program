# Sort given sequence of strings

def main():
    usr = input("Enter the list of items with comma separated: ")
    list =usr.split(",")
    list.sort()
    
    for i in list:
        print(i,end=",")
    print()    


if __name__ == '__main__':
    main()