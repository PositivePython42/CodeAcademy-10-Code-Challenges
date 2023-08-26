"""
Give me the discount Create a function in Python that accepts two parameters.
The first should be the full price of an item as an integer.
The second should be the discount percentage as an integer.
The function should return the price of the item after the discount has been applied.
For example, if the price is 100 and the discount is 20, the function should return 80.
"""

def calculate_discount(price, offer):
    print(f"The discounted price is {price - (price * (offer/100))}.")

while True:
    full_price = int(input("What is the full price of the item : "))
    discount = int(input("What discount is on offer (no more than 100%) : "))
    if discount <= 100:
        calculate_discount(full_price, discount)
    elif discount > 100:
        print("You obviously dont want to use this anymore!")
        break