class Juice(Drink):
    TYPES = {
        "Orange": 2.50,
        "Apple": 2.00,
        "Cranberry": 3.00
    }

    def __init__(self, juice_type, size):
        super().__init__(f"{juice_type} Juice", size, Juice.TYPES[juice_type])