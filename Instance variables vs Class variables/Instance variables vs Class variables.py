class Employee:
    Company_name = "Samparkdesingindia"
    no_of_Employee = 0
    def __init__(self, name, id,):
        self.name = name
        self.id = id
        self.raise_amount = 0.02
        Employee.no_of_Employee +=1
    def ShowEmployeeDetails(self):
        print(f"Employee Name is {self.name} Employee id is {self.id} raise percent is {self.raise_amount}% and his company branch is {self.Company_name} total Employee in Company is {self.no_of_Employee}")


emp1 = Employee("Harry","89A")

emp1.raise_amount = 3

emp1.Company_name = "Hussain Enterprises"

emp2 = Employee("Hussain","689A")

emp2.Company_name = "Samad Enterpries"


emp3 = Employee("Samad","70V")

# emp1.ShowEmployeeDetails()

Employee.ShowEmployeeDetails(emp1)

Employee.ShowEmployeeDetails(emp2)

Employee.ShowEmployeeDetails(emp3)















