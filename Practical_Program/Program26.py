# This python program have a function which returns the sum of two numbers

def add(a,b):
    return a + b

if __name__ == '__main__':
    a = int(input("Enter the num1: "))
    b = int(input("Enter the num2: "))

    print(f"Sum of {a} and {b} is: ",add(a,b))