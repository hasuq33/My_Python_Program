# This Program take multiple inputs and give you output in Uppercase

def main():
    list = []

    while True:
        user_input = input().upper()
        if user_input == '':
            break
        else:
            list.append(user_input)

    for i in list:
        print(i)        

if __name__ == '__main__':
    main()