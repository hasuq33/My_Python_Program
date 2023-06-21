# coding: utf-8 
# Python program to randomely generate list with
# 5 even numbers between 100 and 200 inclusive
# Use random.sample() function

import random

def main():
    x = random.sample([i for i in range(100,201) if i%2 == 0],5)
    print(x)

if __name__ == "__main__":
    main()