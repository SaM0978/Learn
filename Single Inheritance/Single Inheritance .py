class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def makesound(self):
        print(f"Sound made by {self.name}")

class Bird(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def makesound(self):
        print("Chirp")

    def __str__(self):
        return f"{self.name} ({self.species}) - {self.breed}"

bird = Bird("Tweety", "Canary", "Yellow")
bird.makesound()
print(str(bird))


Animal1 = Animal("Dog","German Shephard")

class Cat(Animal):
    def __init__(self, name, species, catpoints):
        super().__init__(name, species)
    def makesound(self):
        return super().makesound()
    
c = Cat("Cattu","Battu","Sattu")

print(c.makesound())