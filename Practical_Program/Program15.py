# # program 15 :

# Write a program that computes the value of a+aa+aaa+aaaa
# with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

def main():
    number = int(input("Enter the number: "))
    
    sum = number
    sum1= sum+(number*10)
    sum2= sum1+(number*100)
    sum3 = sum2+(number*1000)
    finalSum = sum+sum1+sum2+sum3
    print(finalSum)
    

if __name__ == '__main__':
    main()