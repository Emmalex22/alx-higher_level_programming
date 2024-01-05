#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    from calculator_1 import add, subtract, multiply, divide
    answer_add = add(a, b)
    answer_subtract = subtrct(a, b)
    answer_multiply = multiply(a, b)
    answer_divide = divide(a, b)
    print("Addition is:", answer_add)
    print("Subtraction is:", answer_subtract)
    print("Multiplication is:", answer_multiply)
    print("Division is:", answer_divide)
    
