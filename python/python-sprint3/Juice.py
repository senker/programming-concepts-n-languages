class Juice(Drink):
    def __init__(self, name, size):
        self.size = size
        if size == "Small":
            price = 2.0
        elif size == "Medium":
            price = 2.5
        elif size == "Large":
            price = 3.0
        else:
            raise ValueError("Invalid size: {}".format(size))
        super().__init__(name, price)