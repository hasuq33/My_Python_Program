# coding: utf-8
# This python program is work on the formula of f(n) = f(n-1) + 100
# Here f(0) = 1 and give the output of n
def main(n):
    if n == 0:
        return 1
    elif n>0:
        return main(n-1) +100

if __name__ == "__main__":
    n = int(input("Enter the numer: "))
    print(main(n))