# A very simple python program to compare two numbers using functions

from sys import exit

def main():
    check()
    compare(x, y)

def check():
    # prompt user for two numbers
    x = input("x: ")
    y = input("y: ")

    # apply sanity check
    if x.isnumeric() == False and y.isnumeric() == False:
        print("Usage: only real numbers are accepted.")
        exit(1)
    else:
        return x, y

def compare(x, y):
    # TODO
    if x < y:
        return print("x is smaller than y")
    elif x > y:
        return print("x is greater than y")
    else:
        return print("They are the same!")

main()
