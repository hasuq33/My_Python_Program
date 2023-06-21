# coding: utf-8

# This python program is using list comprehension, please write a program generate a 3*5*8 3D
# array whose each element is 0.

def main():
    myArray =[]
    for i in range(3):
        list2 =[]
        for j in range(5):
            list1 =[]
            for k in range(8):
                list1.append("0")

            list2.append(list1)
        myArray.append(list2)

    print(myArray)            

if __name__ == '__main__':
    main()
