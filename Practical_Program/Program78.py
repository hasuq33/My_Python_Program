# Generate a random number list in range between 100 and 200 inclusive and list has only 5 elements

import random

def main():
    x = random.sample(range(100,201),5)
    print(x)

if __name__ == "__main__":
    main()