# This python program checks the passaword is valid or not.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
#here we import re module for search specific words in string
import re 

def validate_password(psw):
    specialSymbols = ['@','#','$','%'] 
    if not re.search("[a-z]",psw):
        return False
    if not re.search("[A-Z]",psw):
        return False
    if not re.search("[0-9]",psw):
        return False
    if not any(char in specialSymbols for char in psw):
        return False
    return psw 

def main():
    psws = input("Enter the passwords with commma separated: ").split(",")
    psw_list = []
    for psw in psws:
        if len(psw) >= 8 and len(psw) <=12:
            validPsw = validate_password(psw)
            psw_list.append(validPsw) 
    for psw in psw_list:
        print(psw,end=" ")
    print()         

if __name__ == '__main__':
    main() 