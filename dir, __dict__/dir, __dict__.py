# x = [1,2,3]

# print(dir(x))

# print(x.__add__)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def fromstr1(c, string):
        return c(string.split("-")[0], int(string.split("-")[1]))
    @classmethod
    def fromstr2(c, string, splitter):
        return c(string.split(splitter)[0], int(string.split(splitter)[1]))


spiltter = "/"

string = "Hussain/23"

p = Person.fromstr2(string, spiltter)

print(p.name,p.age)

print(p.__dict__) # Arrange Format in Dicationary Format

print(help(Person))









