# This python program take two input numbers n1 and n2
# Returns the list of squeare numbers between n1 and n2


def main(n1,n2):
    list = []
    for i in range(n1,n2+1):
        list.append(i**2)
    print(list)    

if __name__ == '__main__':
    n1 = int(input("Enter the n1: "))
    n2 = int(input("Enter the n2: "))
    main(n1,n2)