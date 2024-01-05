#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1

    if num_args == 0:
        print("0 argument.")
        print(".")
    else:
        print(f"{num_args} {'argument' if num_args == 1 else 'arguments'}:")
    for i, arg in enumerate(argv[1:], 1):
        print(f"{i}: {arg}")
