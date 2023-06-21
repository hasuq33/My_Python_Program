def greet(func):
    def inner_func(*args, **kwargs):
        print("Program is initialized:")
        func(*args, **kwargs)
        print("Program is end!")
    return inner_func

@greet
def addNum(a,b):
    print(a+b)

addNum(5,6) 

