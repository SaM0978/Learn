class person:
    def __init__(self, n , o):
        self.name = n
        self.job = o
    def info(self):
        print(f"{self.name} is a {self.job}")

a = person("Harry", "Developer")

b = person("Divya", "HR")

c = person("Hussain", "Saiyan")

a.info()

b.info()

c.info()











