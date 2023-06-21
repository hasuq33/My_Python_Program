# coding: utf-8

# This python program to compress and decompress 
# the string from user input

import zlib

def main(usr):
    compreso = zlib.compress(usr.encode()) # We compress the string 
    print(f'Compressed String: {compreso}')
    decompress = zlib.decompress(compreso).decode() #We decompress the string
    print(f"Decompressed String: {decompress}")


if __name__ == '__main__':
    usr = input("Enter some input here: ")
    main(usr)