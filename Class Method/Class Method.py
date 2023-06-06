class hussain:
    company = "Hussain"  # lowercase company

    def show(self):
        print(f"This is info of {self.name} he works in {self.company}")

    @classmethod
    def ChangeCompany(cls, newCompany):
        cls.company = newCompany

Samad = hussain()
Samad.name = "Samad"
Samad.show()  # output: This is info of Samad he works in Hussain

hussain.ChangeCompany("Apple")  # using class method
Samad.show()  # output: This is info of Samad he works in Apple

print(hussain.company)  # output: Apple
