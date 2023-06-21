# This python program has a function which checks the number 
# is even or odd. If number is even then it will print this is an even
# an even number otherwise it will print This is an odd number.
def oddEeven(num):
    if num%2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number.")    
    

def main():
    num = int(input("Enter the number: "))
    oddEeven(num)
    

if __name__ == "__main__":
    main()