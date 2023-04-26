from typing import Union, Dict

Size = Dict[str, float]

class Tea:
    def __init__(self):
        self.drinks: Union[Dict[str, Dict[str, Size]], None] = {
            "Green Tea": {"Small": 2.00, "Medium": 3.00, "Large": 4.00},
            "Black Tea": {"Small": 2.00, "Medium": 3.00, "Large": 4.00},
            "Herbal Tea": {"Small": 2.50, "Medium": 3.50, "Large": 4.50}
        }

    def display_menu(self):
        print("Tea Menu:")
        for tea_type, sizes in self.drinks.items():
            print(tea_type)
            for size, price in sizes.items():
                print(f"\t{size}: {price}$")

    def get_drink_price(self, drink_kind, drink_size):
        return self.drinks[drink_kind][drink_size]
