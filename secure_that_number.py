"""
Hide the credit card number Write a function in Python that accepts a credit card number.
It should return a string where all the characters are hidden with an asterisk except the last four.
For example, if the function gets sent “4444444444444444”, then it should return “4444”.
"""

asterisk_list = []

def hide_number(unsecure_number):
    ccn_list = list(unsecure_number)
    number_characters_hide = len(unsecure_number) -4
    for i in range(number_characters_hide):
        asterisk_list.append('*')
    
    asterisk_string = ""
    for element in asterisk_list:
        asterisk_string += element
     
    ccn_string = ""
    for element in range(-4, 0, 1):
        ccn_string += ccn_list[element]

    return_numbers = asterisk_string + ccn_string
    print(f"Your secure value is {return_numbers}")

credit_card_number = input("Please input the credit card number : ")
hide_number(credit_card_number)