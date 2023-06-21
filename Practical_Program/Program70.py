# coding: utf-8
# This python program is use assert statements to verify that
# every number in the list [2,4,6,8] is even.

def main():
    myList = [2,4,6,8,7]
    for i in myList:
        assert i%2 == 0
    print("We have verify assertions successfully.")    

if __name__ == '__main__':
    try:
        main()
    except AssertionError :
        print("Assertion statement condition failed!")  
    finally:
        print("Program Ends!")      