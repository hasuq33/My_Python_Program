# This Python program has a class American and subclass Newyorker

def main():
    class American:
        print("I am American.")

    class Newyorker(American):
        print("I am Newyorker.")  

    American()
    Newyorker()      

if __name__ == '__main__':
    main()