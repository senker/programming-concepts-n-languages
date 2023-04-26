class Coffee(Drink):
    def __init__(self, name, size):
        self.size = size
        if size == "Small":
            price = 2.5
        elif size == "Medium":
            price = 3.0
        elif size == "Large":
            price = 3.5
        else:
            raise ValueError("Invalid size: {}".format(size))
        super().__init__(name, price)