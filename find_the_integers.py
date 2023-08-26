"""
Just the numbers Write a function in Python that accepts a list of any length that contains a mix
    of non-negative integers and strings.
The function should return a list with only the integers in the original list in the same order.
"""

import re

def extract_integers_from_list(lst):
    pattern = r'\b\d+\b'  # Regular expression pattern to match integers

    integers = []
    
    for item in lst:
        # Use re.findall to find all matches of the pattern in the item
        matches = re.findall(pattern, str(item))
        # Convert the matched strings to integers and add them to the result list
        integers.extend([int(match) for match in matches])

    return integers

# Test the function
input_list = ["abc", "123", "def", "456", "ghi", "789", "1", "2", "3"]
print(f"The input list is {input_list}.")
result = extract_integers_from_list(input_list)
print(f"The integers in the list are {result}.")  # Output: [123, 456, 789, 1, 2, 3]