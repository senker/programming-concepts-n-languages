class Coffee(Drink):
    TYPES = {
        "Regular": 2.50,
        "Latte": 3.50,
        "Cappuccino": 3.00
    }

    def __init__(self, coffee_type, size):
        super().__init__(f"{coffee_type} Coffee", size, Coffee.TYPES[coffee_type])
