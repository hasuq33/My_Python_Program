# This python program has class name Shape

def main(n1):
    class Shape:
        def __init__(self,length):
            self.length = length

        def area(self):
            return 0

    class Square(Shape):
        def __init__(self,length): 
            self.length = length

        def area(self):
            Area = pow(self.length,2)
            print(f"The area of the square is {Area}.")  

    square = Square(n1)
    square.area()                 

if __name__ == '__main__':
    try:
        n1 = int(input("Enter the length of square: "))
        main(n1)
    except ValueError:
        print("Check the value")    