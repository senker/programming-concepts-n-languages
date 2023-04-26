class Coffee:
    def __init__(self):
        self.drinks: Union[Dict[str, Dict[str, Size]], None] = {
            "Espresso": {"Small": 2.00, "Medium": 3.00, "Large": 4.00},
            "Latte": {"Small": 2.50, "Medium": 3.50, "Large": 4.50},
            "Cappuccino": {"Small": 2.50, "Medium": 3.50, "Large": 4.50},
            "Caramel Macchiato": {"Small": 3.50, "Medium": 4.50, "Large": 5.50}
        }

    def display_menu(self):
        print("Coffee Menu:")
        for coffee_type, sizes in self.drinks.items():
            print(coffee_type)
            for size, price in sizes.items():
                print(f"\t{size}: {price}$")

    def get_drink_price(self, drink_kind, drink_size):
        return self.drinks[drink_kind][drink_size]
