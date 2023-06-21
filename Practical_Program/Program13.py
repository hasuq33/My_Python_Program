# This python program  that will check how many digits and letters are in the given input

def main():
    digit = 0
    letters = 0
    usr = input("Enter your input: ")
    
    text = ""
    # We romeve space from out input
    for index,char in enumerate(usr):
        if usr[index] == " ":
            pass
        else:
            text = text + char

    usr = text          

    for i in usr:
        if i.isdigit():
            digit += 1
        elif i.isalpha():
            letters += 1
        else:
            pass
    print(f"Digits are: {digit}")
    print(f"Letters are: {letters}")        
            
        

if __name__ == '__main__':
    main()