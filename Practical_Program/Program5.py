# Using class we convert inputed strings into UpperCase Strings

def main():
    class UpperCase:
        def __init__(self,value):
            self.value = value
        #str method return a string representation 
        def __str__(self):
            return (self.value).upper()
        def test(self):
            print("Our Program is successfully converted given string value into upper case Value")

    usr = input("Enter the text: ")
    u = UpperCase(usr) 
    print(u) # It print Uppercase value     
    u.test()

if __name__ == '__main__':
    main()