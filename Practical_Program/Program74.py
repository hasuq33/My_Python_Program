# This python program will generate random float number value between 10 and 100 using Python math module.

import random

def main():
    x = round(random.uniform(10,100),2)  
    print(x)

if __name__ == '__main__':
    main()