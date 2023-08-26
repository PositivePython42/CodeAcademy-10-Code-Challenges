"""
Are the Xs equal to the Os? Create a Python function that accepts a string.
This function should count the number of Xs and the number of Os in the string.
It should then return a boolean value of either True or False.

If the count of Xs and Os are equal, then the function should return True.
If the count isn’t the same, it should return False.
If there are no Xs or Os in the string, it should also return True because 0 equals 0.
The string can contain any type and number of characters.
"""

def XO_test(test_this):
    test_list = [i for i in test_this]
    Xs, Os = 0, 0
    
    for element in range(len(test_list)):
        if test_list[element] == "X":
            Xs += 1
        if test_list[element] == 'O':
            Os += 1
    
    if Xs == 0 and Os == 0:
        print('False')
    elif Xs == Os:
        print('True')
    elif Xs != Os:
        print('False')


test_string = input("Enter a string of X and O characters only : ")
XO_test(test_string)