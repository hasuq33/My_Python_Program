# This python program will take a numer in the form of strings and returns the sum of number
def main(n1,n2):
    return int(n1) + int(n2)

if __name__ == '__main__':
    n1 = input("Enter the number n1: ")
    n2 = input("Enter the number n2: ")
    print("The sum of two given number is",main(n1,n2))