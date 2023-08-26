"""
Convert a decimal number into binary Write a function in Python that accepts a decimal number and returns the equivalent binary number.
To make this simple, the decimal number will always be less than 1,024, so the binary number returned will always be less than ten digits long.
"""

BINARY_VALUES = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
binary_number = []

decimal = int(input("Please enter the decimal number (<1024) you want to show in binary : "))

print("\nThis calc uses the Python bin method")
print(bin(decimal))

print("\nThis calc uses a loop to build a list of the binary characters")
for digit in range(len(BINARY_VALUES)):
    if decimal >= BINARY_VALUES[digit]:
        binary_number.append(1)
        decimal -= BINARY_VALUES[digit]
    else:
        binary_number.append(0)

binary_as_string = ''.join(str(x) for x in binary_number)
print(binary_as_string)