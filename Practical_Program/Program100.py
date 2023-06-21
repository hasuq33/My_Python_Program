# coding: utf-8

# This Python program to solve a classic ancient Chinese puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits in a farm.
# How many rabbits and how many chickens do we have?



def SolvedPuzzle(heads,legs):
    for chickens in range(1,legs+1):
        rabbits = heads - chickens
        if(rabbits*4 + chickens*2) == legs:
           print(f"The number of chickens are: {chickens} ") 
           print(f"The number of rabbits are: {rabbits} ") 



def main():
    heads=35
    legs = 94
    SolvedPuzzle(heads,legs)

if __name__ == '__main__':
    main()