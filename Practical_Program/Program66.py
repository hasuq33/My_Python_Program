# coding: utf-8 
# This python program print the sum of fibonacci terms using recursion

def main(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return main(n-2) + main(n-1) 
           

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print(main(n))