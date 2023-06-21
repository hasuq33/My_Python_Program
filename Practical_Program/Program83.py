# coding: utf-8 

# This python program calculates the running time of 1+1 operation 100 times

import timeit
import datetime

def main():
    for _ in range(100):
        c = 1+1
        print(c)

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    stop = timeit.default_timer()
    print(stop - start)
   