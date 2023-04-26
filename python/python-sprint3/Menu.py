from Tea import Tea
from Coffee import Coffee
from Juice import Juice

class Menu:
    def __init__(self):
        self.drinks = {
            "Coffee": Coffee(),
            "Tea": Tea(),
            "Juice": Juice()
        }

    def display_menu(self):
        print("Menu:")
        for drink_type, drink_obj in self.drinks.items():
            print(drink_type)
            for drink_kind, sizes in drink_obj.drinks.items():
                print(f"\t{drink_kind}:")
                for size, price in sizes.items():
                    print(f"\t\t{size}: {price}$")

    def get_drink_price(self, drink_type, drink_kind, drink_size):
        return self.drinks[drink_type].drinks[drink_kind][drink_size]
