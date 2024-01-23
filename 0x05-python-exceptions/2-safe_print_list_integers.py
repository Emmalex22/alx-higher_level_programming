#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0
    try:
        for i in range(x):
            val = my_list[i]
            if isinstance(val, int):
                print("{:d}".format(val), end=" ")
                printed_integers += 1
    except IndexError:
        pass
    finally:
        print()
        return printed_integers
