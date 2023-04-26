from Menu import Menu


class Order:
    def __init__(self, menu):
        self.menu = menu
        self.order_items = []


    def add_to_order(self, drink_type, drink_kind, drink_size, quantity):
        self.order_items.append({
            'drink_type': drink_type,
            'drink_kind': drink_kind,
            'drink_size': drink_size,
            'quantity': quantity
    })

    def calculate_total_price(self):
        total_price = 0
        for item in self.order_items:
            drink_type = item['drink_type']
            drink_kind = item['drink_kind']
            drink_size = item['drink_size']
            quantity = item['quantity']
            drink_price = self.menu.get_drink_price(drink_type, drink_kind, drink_size)
            item_price = drink_price * quantity
            total_price += item_price
        return total_price

    def display_order_summary(self):
        print("Order summary:")
        for item in self.order_items:
            drink_type = item['drink_type']
            drink_kind = item['drink_kind']
            drink_size = item['drink_size']
            quantity = item['quantity']
            drink_price = self.menu.get_drink_price(drink_type, drink_kind, drink_size)
            item_price = drink_price * quantity
            print(
                f"{quantity} x {drink_size} {drink_type} {drink_kind} ({drink_price}$ each): {item_price}$")
        total_price = self.calculate_total_price()
        print(f"Total price: {total_price}$")
