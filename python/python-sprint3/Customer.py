class Customer:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.cart = []

    def get_name(self):
        return self.name

    def get_budget(self):
        return self.budget

    def get_cart(self):
        return self.cart

    def add_to_cart(self, drink):
        self.cart.append(drink)

    def remove_from_cart(self, drink):
        if drink in self.cart:
            self.cart.remove(drink)

    def calculate_total(self):
        total = 0
        for drink in self.cart:
            total += drink.get_price() * drink.get_quantity()
        return total

    def checkout(self):
        total = self.calculate_total()
        if total > self.budget:
            return False
        self.budget -= total
        for drink in self.cart:
            drink.set_quantity(drink.get_quantity() - 1)
        self.cart = []
        return True