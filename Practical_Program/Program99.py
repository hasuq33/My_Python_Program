# coding: utf-8
# This python program which prints all permutations of [1,2,3]

from itertools import permutations

def main():
    print(list(permutations(range(1,4),2)))

if __name__ == '__main__':
    main()