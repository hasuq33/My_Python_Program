# This python program has a class named American which has
# a static method called printNationality.
def main():

    class American:
        def __init__(self):
            pass
        @staticmethod
        def printNationality():
            print("American National")


    a1 = American()
    a1.printNationality()        
        

if __name__ == '__main__':
    main()