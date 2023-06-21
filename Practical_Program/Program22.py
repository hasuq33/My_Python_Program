# This python program about to calculate the frequency of word in user input 

def freqWord(usr):
    usrList = usr.split()

    #Making sets for removinf duplucates words
    wordSet = set(usrList)
    
    for word in wordSet:
        print(word,":",usrList.count(word))


def main():
    usr = input("Type some text here: ")
    freqWord(usr)

if __name__ == "__main__":
    main()