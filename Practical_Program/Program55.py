# This python program raise the runtime error 
def main(a,b):
    if b == 0:
        raise RuntimeError("Cannot divide by zero!")
    else:
        c = a/b
        print(f"The {a} is divided by {b} and the answer is {c}.")

if __name__ == "__main__":
    try:
         main(10,0)
    except RuntimeError as e:
        print(f"Runtime error Occured as a {e}.")