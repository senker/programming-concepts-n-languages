from abc import ABC, abstractmethod

class CaffeineDrink(ABC):
    def __init__(self, description, size):
        self.description = description
        self.size = size

    def drink_info(self):
        print(f"{self.size} {self.description}")
    
    @abstractmethod
    def get_price(self):
        pass