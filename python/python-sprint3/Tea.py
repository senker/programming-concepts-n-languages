class Tea(Drink):
    TYPES = {
        "Green": 2.00,
        "Black": 1.50,
        "Herbal": 2.50
    }

    def __init__(self, tea_type, size):
        super().__init__(f"{tea_type} Tea", size, Tea.TYPES[tea_type])
