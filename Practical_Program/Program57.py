# This python program has a custom exception class which takes a string message as attribute

def main():
    
    class ExceptionError(Exception):

        def __init__(self, message):
            self.message = message
    try:
        ExceptionError()
    except Exception:
        print("We caught an exception")
    # except RuntimeError :
    #     print("This is runtime error") 
    finally:
        print("Our program is finished!")               

if __name__ == "__main__":
    main()