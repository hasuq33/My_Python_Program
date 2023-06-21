# This python program is basic class which have a atleast one parameter and set the value in it
def main():
    class Property:
        def __init__(self,name):
            self.name = name

        def __str__(self):
            return f"The given property name is: {self.name}"   
    
    p1 = Property("Pratik Mall")
    print(p1)
    print(p1.name)

if __name__ == '__main__':
    main()