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
    def __len__(self):
        i = 0
        for c in self.name:
            i += 1
        return i
