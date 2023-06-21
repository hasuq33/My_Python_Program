# This python program calculate the area of circe using class name circles.
def main(n1):
    class Circle:

        def __init__(self,radius):
            self.radius = radius

        def area(self):
            Area = (3.14)*(pow(self.radius,2))  
            print(f"The area of circle is {Area}")

    c = Circle(n1) 
    c.area()       



if __name__ == "__main__":
    n1 = int(input("Enter the radius of the circle: "))
    main(n1)