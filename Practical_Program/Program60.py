# This python program find digits from the given string and give the list of digits

import re

# Method 1
def main(usr):
    number = re.findall('[0-9]+',usr)
    print(number)

# Method 2
def main1(usr):
    myList = []

    for i in usr:
        if  i.isdigit():
            myList.append(i)
    
    print(myList)

if __name__ == '__main__':
    usr = input("Enter some text here: ")
    main(usr)
    main1(usr)