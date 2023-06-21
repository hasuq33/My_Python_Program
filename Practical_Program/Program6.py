from math import sqrt

def main():
    C=50
    H=30
    usr = input("Enter the nubers: ")
    list = usr.split(",")
    for i in list:
       D = int(i)
       intermediateValue = ((2*C*D)/H)   
       print(int(sqrt(intermediateValue)),end=",")
    print()       


if __name__ == '__main__':
    main()