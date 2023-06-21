# This python program will tell you that howmant uppercase and lowercase in input

def main():
    usr = input("Enter some text: ")
    upper = lower = 0

    for i in usr:
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1

    print(f"UPPER CASE: {upper}")
    print(f"Lower CASE: {lower}")            


if __name__ == '__main__':
    main()