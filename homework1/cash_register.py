"""

TASK 1

Write a class to represent a Cash Register.
Your class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""


class CashRegister:

    def __init__(self):

        self.total_items = {}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item, price):
        self.total_items.update({item: price})
        return self.total_items

    def remove_item(self, item):
        self.total_items.pop(item)
        return self.total_items

    def apply_discount(self):
        discount_amount = sum(self.total_items.values()) - self.discount
        print(f"Your discount is: £{discount_amount}.")
        return discount_amount

    def get_total(self):
        total_price = sum(self.total_items.values()) - self.discount
        print(f"Your total amount is £{total_price}")
        return total_price

    def show_items(self):
        print(f"Your items are {self.total_items}")
        return self.total_items

    def reset_register(self):
        self.total_items.clear()
        self.discount = 0
        self.total_price = 0
        print(f"Transaction cleared")


# EXAMPLE code run:
shopping_trolley = CashRegister()

shopping_trolley.add_item('jeans', 12.99)
shopping_trolley.add_item('jumper', 15.99)
shopping_trolley.show_items()
shopping_trolley.remove_item('jumper')
shopping_trolley.show_items()
shopping_trolley.reset_register()
shopping_trolley.show_items()
shopping_trolley.add_item('perfume', 49.99)
shopping_trolley.add_item('moisturiser', 50.99)
shopping_trolley.show_items()
shopping_trolley.get_total()
shopping_trolley.apply_discount()
shopping_trolley.get_total()