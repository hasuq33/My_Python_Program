# coding: utf-8
# This python program is check the number is divisible by 5 and 7 using generator and retuns the
# and returns the result comma separated 

def main(n):

    def gen(n):
        yield n

    myList = []

    for i in range(n):
        vlue = gen(i)
        num= vlue.__next__()

        if num %7 == 0 and num%5 == 0:
            myList.append(str(i))

    print(",".join(myList))        


if __name__ == "__main__":
    n = int(input("Enter the number: "))
    main(n)