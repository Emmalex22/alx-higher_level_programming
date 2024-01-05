#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    from calculator_1 import add, sub, mul, div
    answer_add = add(a, b)
    answer_sub = sub(a, b)
    answer_mul = mul(a, b)
    answer_div = div(a, b)
    print("Addition is:", answer_add)
    print("Subtraction is:", answer_sub)
    print("Multiplication is:", answer_mul)
    print("Division is:", answer_div)
