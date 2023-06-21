# This python program will compute 5/0 and try to except to catch the exception

def main(n1,n2):
    n3 = n1/n2
    return n3    

if __name__ == "__main__":
    try:
        n1= int(input("Enter the number n1: "))
        n2 = int(input("Enter the number n2: "))
        main(n1,n2)
    except ZeroDivisionError as e:
        print("You can not divide n1 by zero give prope value to n2: ")
    finally:
        print("Our program is finished!")    
