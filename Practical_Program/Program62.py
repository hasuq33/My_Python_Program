def main(usr):
    myStr = usr.encode('utf-8')
    print(myStr)
    # print(myStr.decode('utf-8'))
if __name__ == "__main__":
    usr = input("Enter some text here...")
    main(usr)