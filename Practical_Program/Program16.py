# This python program use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9


def main():
    numbers = input("Enput numbers with comma-separated: ").split(",")
    list(numbers)
    oddNumList = []
    for i in numbers:
        num = int(i)
        if num%2 == 0:
            oddNumList.append(i)

    for index,i in enumerate(oddNumList):
        if index == len(oddNumList)-1:
            print(i,end=" ")
        else:
            print(i,end=",")    
    print()           

if __name__ == "__main__":
    main()