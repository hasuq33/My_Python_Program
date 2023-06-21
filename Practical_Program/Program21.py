#  This python program will check robots movements from (0,0)
from math import sqrt
def main():

    pos = [0, 0]
    while True:
        up = input("UP: ")
        down = input("DOWN: ")
        left = input("LEFT: ")
        right = input("RIGHT: ")
        
        if up == "" and down == "" and left == "" and right == "":
            break

        pos[0]+= int(up)
        pos[0]-=int(down)
        pos[1]+= int(left)
        pos[1]-= int(right)

    value = sqrt(pow(pos[0], 2) + pow(pos[1], 2))
    final_value = int(value)
    print("final value is: ", final_value)    

if __name__ == '__main__':
    main()