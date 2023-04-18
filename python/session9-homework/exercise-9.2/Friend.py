from Contact import Contact
from AddressHolder import AddressHolder

class Friend(Contact, AddressHolder):
    def __init__(self, name, email, phone, street, post_code, city):
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, post_code, city)
        self.phone = phone

    def __str__(self):
        return f"{self.name} ({self.email}, {self.phone}) {self.street} {self.post_code} {self.city}"

friend1 = Friend("Jane Doe", "jane@example.com", "555-1234", "123 Main St", "12345", "Anytown")
print(friend1)