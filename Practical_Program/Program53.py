# This python program has a class name Rectangle which take two parameter 
# length and width and returns the area of the rectangle

def main(n1,n2):
    class Rectangle:

        def __init__(self,length,width):
            self.length = length
            self.width = width

        def area(self):
            Area = self.length * self.width
            print(f"The are of rectangle is {Area}")

    Rect = Rectangle(n1,n2) 
    Rect.area()           

if __name__ == '__main__':
    n1 = int(input("Enter the length of the rectangle: "))
    n2= int(input("Enter the width of the rectangle: "))
    main(n1, n2)