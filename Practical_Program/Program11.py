# program 11 :

# Write a program which accepts a sequence of comma
# separated 4 digit binary numbers as its input and then
# check whether they are divisible by 5 or not. The numbers
# that are divisible by 5 are to be printed in a comma
# separated sequence.

# Example:
# 0100,0011,1010,1001

# Then the output should be:
# 1010# 

# This function returns the decimal number from binary numbers
def decimalBinary(num):
    sum = 0
    l = list(num)
    l.reverse() # For getting proper index to multiply numbers
    for i in range(len(l)):
        sum = sum + int(l[i])*pow(2,i)
    return sum 
   
# This our our main function which will check the given binary number is divisible by 5 or not and returns in the form of thr lists 
def main():
    list = []
    inputNumlist = input("Enter the binary number in sequence with comma separated: \n").split(",")
    for n in inputNumlist:
        decimalNumber = decimalBinary(n)
        if (decimalNumber % 5 == 0):
            list.append(n)
    return list


if __name__=='__main__':
   numbers =  main()
   for i in numbers:
       print(i,end=" ")  
   print()   