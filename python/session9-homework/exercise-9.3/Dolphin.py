from Fish import Fish

class Dolphin(Fish):
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating fish")

    def swim(self):
        print(f"{self.name} is swimming")
        
dolphin = Dolphin("Flipper")
dolphin.eat()
dolphin.swim()