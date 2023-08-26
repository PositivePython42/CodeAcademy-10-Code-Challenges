"""
Count the vowels in a string
Create a function in Python that accepts a single word and returns the number of vowels in that word.
In this function, only a, e, i, o, and u will be counted as vowels — not y.
"""

VOWELS = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
number_of_vowels = 0

phrase = input("Enter the phrase you would like to count the vowels in : ")

for element in phrase:
    if element in VOWELS:
        number_of_vowels += 1
        
print(f"Your phrase has {number_of_vowels} vowels in it.")