#This program is for finding the factorial of number
def factorial(a):
    if a == 1:
        return 1
    else:
        return factorial(a-1)*a
    
if __name__ == '__main__':
    print("This program is for finding the factorial of number")
    a = int(input("Enter the number: "))
    print(factorial(a))