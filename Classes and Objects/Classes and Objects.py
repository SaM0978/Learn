class Person:
    name = "Samad"
    job = "Student"
    networth = 10
    seatnumber = "30A"
    def info(self):
        print(f"{self.name} is a {self.job} his networth is {self.networth} his seat no is {self.seatnumber}")

a = Person()

b = Person()

a.name = "Hussain"

a.job = "Youtuber"

a.networth = "$20"

a.seatnumber = "50G"

b.name = "Jason"

b.networth = "$300"

b.seatnumber = "67D"

b.job = "HR"

a.info()

b.info()



























