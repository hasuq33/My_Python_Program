# This program prints 2-D Arrays 
def main():
    row = int(input('How many rows do you want: ')) #5
    column = int(input('How many columns do you want: ')) #3
    arr = []
    
    for i in range(row):  
        a = []  
        for j in range(column):
            a.append(i*j)
        arr.append(a)
    print(arr)     

if __name__ == '__main__':
    main()