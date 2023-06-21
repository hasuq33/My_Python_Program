# Write a python function which converts integers into strings
def main(usr):
    return str(usr)

if __name__ == '__main__':
    usr = int(input("Enter the number: "))
    string = main(usr)
    print(f"The type of {usr} is: ",type(string))