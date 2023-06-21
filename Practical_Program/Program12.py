# Write a python program that checks each digit in number must be divisible by 2 
# Check each numbers in range between 1000 to 3000

def main():
    n1 = int(input("Enter the starting number: "))
    n2 = int(input("Enter the ending number: "))
    list =[]
    for i in range(n1, n2+1):
        sum =0
        temp = i
        while temp>0:
            digit = temp%10
            sum += digit
            temp = temp//10 
        if sum%2 == 0:
            list.append(i)
    print(list)        
         

if __name__ == '__main__':
    main()