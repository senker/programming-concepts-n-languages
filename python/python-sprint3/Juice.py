class Juice:
    def __init__(self):
        self.drinks: Union[Dict[str, Dict[str, Size]], None] = {
            "Orange Juice": {"Small": 2.00, "Medium": 3.00, "Large": 4.00},
            "Apple Juice": {"Small": 2.00, "Medium": 3.00, "Large": 4.00},
            "Grapefruit Juice": {"Small": 2.50, "Medium": 3.50, "Large": 4.50}
        }

    def display_menu(self):
        print("Juice Menu:")
        for juice_type, sizes in self.drinks.items():
            print(juice_type)
            for size, price in sizes.items():
                print(f"\t{size}: {price}$")

    def get_drink_price(self, drink_kind, drink_size):
        return self.drinks[drink_kind][drink_size]