# This python program extract the company name from the email address
import re

# Method 1 using the re expression 
def main1(n1):
    companyName = re.findall(r'\w+[.]',n1)[0][:-1]
    print(companyName)

# Method 2 using the index function
def main2(n1):
    for i in n1.split():
        s = i.index("@") # Slice begins +1 avoiding the @
        e = i.index(".") # Slice end and by default not accounting it
    # print(s)
    # print(e)    
    print(n1[s+1:e])    

if __name__ == "__main__":
    n1 = input("Enter the email address in the format of 'username@company.com': ")
    main1(n1)
    main2(n1)