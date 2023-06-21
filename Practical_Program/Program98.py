# coding: utf-8

# This python program is accept the string from console and print characters that evenly index


def main():
    usr = input("Enter some text here...")
    print(usr[::2])


if __name__ == "__main__":
    main()