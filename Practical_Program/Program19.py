# This is a python program which sorts the tuple on the basis of name, age and score

# This function sorts the lists of tuple on the basis of name, age and score
def sortTupple(list):
    return(sorted(list, key=lambda x: x[0]))

def main():
    list = []
    while True:
        usr = input("Enter the name, age and score with comma separated: ")
        if usr == "":
            break
        nusr = usr.split(',') # Remove the comma
        new_usr = tuple(nusr) # Make a new tuple
        list.append(new_usr)  # Each tuple appends in list 

    print(sortTupple(list))
        

if __name__ == '__main__':
    main()