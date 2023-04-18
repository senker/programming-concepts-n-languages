from CaffeineDrink import CaffeineDrink

class Coffee(CaffeineDrink):
    def __init__(self, description, size, quantity, tax_rate):
        CaffeineDrink.__init__(self, description, size)
        self.quantity = quantity
        self.tax_rate = tax_rate
    
    def get_price(self):
        if self.size == "Small":
            price_per_unit = 15
        elif self.size == "Medium":
            price_per_unit = 20
        elif self.size == "Large":
            price_per_unit = 25
        else:
            raise ValueError(f"Invalid size: {self.size}")

        return (self.quantity * price_per_unit) * self.tax_rate

# Testing
# Create a Coffee object and print its information
my_coffee = Coffee("Latte", "Medium", 2, 1.1)
my_coffee.drink_info()

# Calculate and print the price of the coffee
coffee_price = my_coffee.get_price()
print(f"The price of the coffee is {coffee_price}.")