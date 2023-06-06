# Super Can Excute Parent Method

class ParentClass:
    def parentmethod(self):
        print("This Is Parent Class")

class ChildClass(ParentClass):
    def parentmethod(self):
        print("This Is A Child Class")
        return super().parentmethod()
    def childmethod(self):
        print("Nothinig")
        super().parentmethod()
            
c = ChildClass()

c.parentmethod()

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Progammer(Employee):
    def __init__(self, name, id, lang):
        self.name = name
        super(). __init__(name, id)
        self.lang = lang

c = Progammer("Hussain","34","Python")

d = Employee("Samad","5G",)

print(c.name,c.id,c.lang)

print(d.name,d.id)















