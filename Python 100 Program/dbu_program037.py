#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 37 :

# Define a function which can generate and print a list
# where the values are square of
# numbers between 1 and 20 (both included).

# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.


def main(num1, num2):

    li = list()
    if num1 < num2:
        for cnt in range(num1, num2 + 1):
            li.append(cnt ** 2)
        print li

    else:
        print 'Ending range must be greater than starting range'

if __name__ == '__main__':
    try:
        num1 = int(raw_input('Enter starting range: '))
        num2 = int(raw_input('Enter ending range: '))
        main(num1, num2)
    except ValueError:
        print 'check value'
