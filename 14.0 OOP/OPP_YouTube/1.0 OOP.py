# # OPP
#
# item1 = 'Phone'
# item_price = 100
# item1_quantity = 5
# item1_price_total = item_price * item1_quantity
# item1_price_discount = item1_price_total * 0.95
#
# print(type(item1))  # This is an instance of string class
# print(type(item_price))  # This is an instance of integer class
# print(type(item1_quantity))  # This is an instance of string class
# print(type(item1_price_total))  # This is an instance of string class
# print(type(item1_price_discount))  # This is an instance of float class

# =============================================================================

# Creating Classes


class Item:
    pass


item1 = Item()  # This is how to create an instance from a class!

print(type(item1))  # This is an instance of Item class

#  Attributes are things the object have
# we can give it attributes to our item instance or object

item1.name = 'Coke'  # This is a name attribute given to the item
item1.price = 100  # This is a price attribute given to the item
item1.quantity = 4  # This is a quantity attribute given to the item

# attribute of an instance might not be a class of that instance

print(type(item1.name))  # This attribute has a class of str
print(type(item1.price))  # This attribute has a class of int
print(type(item1.quantity))  # This attribute has a class of int

# =============================================================================
# Methods are things instances can do, that is functions

# First let us create another object from the class
item2 = Item()
item2.name = 'Fanta'  # This is a name attribute given to the item
item2.price = 240  # This is a price attribute given to the item
item2.quantity = 9  # This is a quantity attribute given to the item

item3 = Item()
item3.name = 'Fanta'  # This is a name attribute given to the item
item3.price = 240  # This is a price attribute given to the item
item3.quantity = 9  # This is a quantity attribute given to the item
