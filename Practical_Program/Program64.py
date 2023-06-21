# coding: utf-8
# This python program compute 1/2+2/3+3/4+...+n/n+1
# with a given n input by console (n>0).

def main(n):
    sum = 0
    for i in range(1,n+1):
        num = round(float((i)/(i+1)),2)
        sum += num

    print(sum)    


if __name__ == '__main__':
    n = int(input("Enter the number: "))
    main(n)