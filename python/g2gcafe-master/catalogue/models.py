class Catalogue:
    def __init__(self):
        self.drinks = {
            "Espresso": {"Small": 2.00, "Medium": 3.00, "Large": 4.00},
            "Latte": {"Small": 2.50, "Medium": 3.50, "Large": 4.50},
            "Cappuccino": {"Small": 2.50, "Medium": 3.50, "Large": 4.50},
            "Caramel Macchiato": {"Small": 3.50, "Medium": 4.50, "Large": 5.50},
            "Green Tea": {"Small": 2.00, "Medium": 3.00, "Large": 4.00},
            "Black Tea": {"Small": 2.00, "Medium": 3.00, "Large": 4.00},
            "Herbal Tea": {"Small": 2.50, "Medium": 3.50, "Large": 4.50},
            "Orange Juice": {"Small": 2.00, "Medium": 3.00, "Large": 4.00},
            "Apple Juice": {"Small": 2.00, "Medium": 3.00, "Large": 4.00},
            "Grapefruit Juice": {"Small": 2.50, "Medium": 3.50, "Large": 4.50}
        }
        self.price = 0

    def display_menu(self):
        menu = []
        for drink_type, sizes in self.drinks.items():
            drink_sizes = []
            for size, price in sizes.items():
                drink_sizes.append((size, price))
            menu.append((drink_type, drink_sizes))
        return menu

    def get_drink_price(self, drink_kind, drink_size):
        return self.drinks[drink_kind][drink_size]

    def set_price(self, drink_kind, drink_size, quantity):
        drink_price = self.get_drink_price(drink_kind, drink_size)
        self.price += drink_price * quantity
