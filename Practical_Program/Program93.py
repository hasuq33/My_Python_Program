# coding: utf-8

# This python program performs intersection operation between two given lists 

def main():
    List1 = [1,3,6,78,35,55]
    List2 = [12,24,35,24,88,120,155]
    x1 = set(List1)
    x2 = set(List2)
    
    x = x1.intersection(x2)
    print(x)
    
if __name__ == '__main__':
    main()