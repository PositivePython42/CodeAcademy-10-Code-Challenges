"""
Repeat the characters
Create a Python function that accepts a string.
The function should return a string, with each character in the original string doubled.
If you send the function “now” as a parameter, it should return “nnooww,” and
    if you send “123a!”, it should return “112233aa!!”.
"""

def string_doubler(entry_string):
    exit_list = []
    exit_string = ""
    
    for element in entry_string:
        exit_list.append(element)
        exit_list.append(element)
    
    for element in exit_list:
        exit_string += element
    
    print(exit_string)

user_string = input("Type in your string and it will magically double! : ")
string_doubler(user_string)