from Menu import Menu
from Order import Order

# create menu object
menu = Menu()

# create order object
order = Order(menu)

# display menu to user
menu.display_menu()

# get user input for drink order
while True:
    drink_type = input("Enter drink type (e.g. Coffee, Tea, Juice): ")
    drink_type_kind = input("Enter the kind of drink (e.g. Machiatto, Latte, Green Tea etc.): ")
    drink_size = input("Enter drink size (e.g. Small, Medium, Large): ")
    quantity = input("Enter quantity: ")

    # add drink to order
    order.add_to_order(drink_type, drink_type_kind, drink_size, int(quantity))

    # ask user if they want to add another drink
    add_another = input("Add another drink? (y/n): ")
    if add_another.lower() == "n":
        break

# display order summary and total price
order.display_order_summary()