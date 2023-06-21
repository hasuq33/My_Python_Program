# coding: utf-8

# This python program has a class Person and its two child classes: Male and Female. All
# classes have a method "getGender" which can print "Male" for Male class
# and "Female" for Female class.

def main():
    class Person:
        def __init__(self):
            pass
        def getGender(self):
            pass

    class Male(Person):
        def getGender(self):
            print("Male")
               
    class Female(Person):
        def getGender(self):
            print("Female")

    Mle = Male()
    Fmle = Female()

    Mle.getGender()       
    Fmle.getGender()       



if __name__ == '__main__':
    main()