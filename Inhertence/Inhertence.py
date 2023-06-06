class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def ShowEmployeeDetails(self):
        print(f"Employee Name is {self.name} Employee id is {self.id}")


Hussain = Employee("Hussain", "45F")

Hussain.ShowEmployeeDetails()

class Programme(Employee):
    @staticmethod
    def showLanguage():
        print("The Default Language is Python")

Samad = Programme("Name", "id")

Samad.showLanguage()

Samad.ShowEmployeeDetails()
