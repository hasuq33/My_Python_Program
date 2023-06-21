#!/usr/bin/env python
# -*- coding: utf-8 -*-

# program 77:

# Please write a program to output a random number,
# which is divisible by 5 and 7, between 0 and 10
# inclusive using random module and list comprehension.

# Hints:
# Use random.choice() to a random element from a list.

import random


def main(num1, num2):
    if num1 < num2:
        print random.choice([cnt for cnt in range(num1, num2 + 1)
                             if cnt % 5 == 0 and cnt % 7 == 0])
    else:
        print 'Ending Range must be greater than Starting Range...'

if __name__ == '__main__':
    try:
        num1 = int(raw_input('Enter Starting Range: '))
        num2 = int(raw_input('Enter Ending Range: '))
        main(num1, num2)
    except ValueError:
        print 'Check Value'
