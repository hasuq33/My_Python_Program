# program 20 :

# Define a class with a generator which can iterate the numbers,
# which are divisible by 7, between a given range 0 and n.

def main():
    class Generator:
        def __init__(self,n):
            self.n = n 
        def divisible(self):
            for i in range(1,self.n):
                if i%7 ==0:
                    print(i,end=" ")
            print()  

    num = int(input("Enter the number: "))
    d = Generator(num)
    d.divisible()

if __name__ == '__main__':
    main()