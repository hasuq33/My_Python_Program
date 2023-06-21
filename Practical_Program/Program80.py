# coding: utf-8

# Python program to generate a list of 5 number in range between 1 and 1000 
# which is divisible by 5 and 7

import random

def main():
    x = random.sample([ i for i in range(1,1001) if i%5==0 and i%7 == 0 ],5)
    print(x)

if __name__ == "__main__":
    main()