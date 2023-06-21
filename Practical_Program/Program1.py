# This program check that number is divisible by 7 but not by 5 in range between 2000 and 3200

if __name__ == "__main__":
    for i in range(2000,3201):
        if i % 7 == 0 and i%5 != 0:
            print(i,end=",")
    print()       
    