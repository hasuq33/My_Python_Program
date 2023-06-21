# coding: utf-8

# This python program to generate all sentences where
# subject is in ["I", "You"] and verb is in ["Play", "Love"]
# and the object is in ["Hockey","Football"].

def main():
    subjects = ["I", "You"]
    verbs = ["Play", "Love"]
    objects = ["Hockey","Football"]

    for i in subjects:
        for j in verbs:
            for k in objects:
                print(f"{i} {j} {k}.")


if __name__ == "__main__":
    main()