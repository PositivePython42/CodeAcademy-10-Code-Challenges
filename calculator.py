"""
Create a calculator function Write a Python function that accepts three parameters.
The first parameter is an integer.
The second is one of the following mathematical operators: +, -, /, or *.
The third parameter will also be an integer.
The function should perform a calculation and return the results.
For example, if the function is passed 6 and 4, it should return 24.
"""

def add(one, two):
    print(one + two)
    
def subtract(one, two):
    print(one - two)
    
def divide(one, two):
    print(one / two)

def multiply(one, two):
    print(one * two)

numberone = int(input("Please enter your fiurst number : "))
numbertwo = int(input("Please enter your second number : "))
operator = input("Please enter your operator (+ - / or *) : ")

if operator == "+":
    add(numberone, numbertwo)
elif operator == "-":
    subtract(numberone, numbertwo)
elif operator == "/":
    divide(numberone, numbertwo)
elif operator == "*":
    multiply(numberone, numbertwo)
else:
    print("Incorrect operator entered, please run again!")