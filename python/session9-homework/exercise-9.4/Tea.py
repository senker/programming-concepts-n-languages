from CaffeineDrink import CaffeineDrink


class Tea(CaffeineDrink):
    def __init__(self, description, size, quantity):
        CaffeineDrink.__init__(self, description, size)
        self.quantity = quantity

    def get_price(self):
        if self.size == "Small":
            price_per_unit = 10
        elif self.size == "Medium":
            price_per_unit = 15
        elif self.size == "Large":
            price_per_unit = 20
        else:
            raise ValueError(f"Invalid size: {self.size}")

        return self.quantity * price_per_unit

# Testing
# Create a Tea object and print its information
my_tea = Tea("Green tea", "Small", 3)
my_tea.drink_info()

# Calculate and print the price of the tea
tea_price = my_tea.get_price()
print(f"The price of the tea is {tea_price}.")