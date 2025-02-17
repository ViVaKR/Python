#! /usr/bin/env python

if __name__ == "__main__":
    print("This is If.py")
else:

    def if_statement():
        x = int(input("Please enter an integer: "))

        if x < 0:
            x = 0
            print("Negative changed to zero")
        elif x == 0:
            print("Zero")
        elif x == 1:
            print("Single")
        else:
            print("More")
