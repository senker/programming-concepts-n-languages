from Drink import Drink


class Menu:
    def __init__(self):
        self.drinks = {
            "Coffee": {
                "Espresso": {"Small": 2.00, "Medium": 3.00, "Large": 4.00},
                "Latte": {"Small": 2.50, "Medium": 3.50, "Large": 4.50},
                "Cappuccino": {"Small": 2.50, "Medium": 3.50, "Large": 4.50},
                "Caramel Macchiato": {"Small": 3.50, "Medium": 4.50, "Large": 5.50}
            },
            "Tea": {
                "Green Tea": {"Small": 2.00, "Medium": 3.00, "Large": 4.00},
                "Black Tea": {"Small": 2.00, "Medium": 3.00, "Large": 4.00},
                "Herbal Tea": {"Small": 2.50, "Medium": 3.50, "Large": 4.50}
            },
            "Juice": {
                "Orange Juice": {"Small": 2.00, "Medium": 3.00, "Large": 4.00},
                "Apple Juice": {"Small": 2.00, "Medium": 3.00, "Large": 4.00},
                "Grapefruit Juice": {"Small": 2.50, "Medium": 3.50, "Large": 4.50}
            }
        }

    def display_menu(self):
        print("Menu:")
        for drink_type, sizes in self.drinks.items():
            print(drink_type)
            for size, price in sizes.items():
                print(f"\t{size}: {price}$")

    def get_drink_price(self, drink_type, drink_kind, drink_size):
        return self.drinks[drink_type][drink_kind][drink_size]

    def add_drink_type(self, drink_type, size_prices):
        self.drinks[drink_type] = size_prices
