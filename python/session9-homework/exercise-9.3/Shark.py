from Fish import Fish

class Shark(Fish):
    def __init__(self, name, place_found):
        self.name = name
        self.place_found = place_found
    
    def eat(self):
        print(f"{self.name} the shark is eating")

    def swim(self):
        print(f"{self.place_found} is where the shark is found")

shark = Shark("Jaws", "Atlantic Ocean")
shark.eat()
shark.swim()