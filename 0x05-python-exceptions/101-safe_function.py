#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        ex_f = fct(*args)
        return ex_f
    except Exception as x:
        print("Exception: {}".format(x), file=sys.stderr)
        return None
