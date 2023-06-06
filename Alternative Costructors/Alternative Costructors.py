class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))
    
    @classmethod
    def fromstr2(cls, string, spliting_value):
        return cls(string.split(spliting_value)[0], int(string.split(spliting_value)[1]))

    def show(self):
        print(f"Name Of The Employee Is {self.name} And His Salary Is {self.salary}")


string = "John-₹12000"

e = employee.fromstr(string)

e.show()

string2 = "Hussain-₹123000"

e2 = employee.fromstr(string2)

e2.show()

info = "Samad/₹24000"

split = "/"

e3 = employee.fromstr2(info,split)

e3.show()





























