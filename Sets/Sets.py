# Sets

a = input("Enter Name Of Employee Who has Not Gotten Salary: ")

b = input("Enter Name Of Employee Who has Not Gotten Salary: ")

c = input("Enter Name Of Employee Who has Not Gotten Salary: ")

if a or b or c == "sam":
     a = "Samad" 
    
     b = "Samad"
    
     c = "Samad"
else:
     a,b,c = 0

a = a.capitalize()

b = b.capitalize()

c = c.capitalize()

Employee_Salary = {a,b,c}

print(Employee_Salary)

l = {"ff","fg","2",'2'}

print(l)

Set = set()

print(type(Set))

for value in l:
    print(value)

s1 = {"Tokyo","Seol","Osaka"}

s2 = {"Ohio","New York",}

print(s1.union(s2))

ss1 = {"Tokyo","Seol","Madrid"}

ss2 = {"Ohio","Tokyo","Madrid"}

print(s1.intersection(s2))

sa1 = {"Tokyo","Seol","Madrid"}

sa2 = {"Ohio","Tokyo","Madrid"}

Cities3 = sa1.symmetric_difference(sa2)

print(Cities3)

sa1 = {"Tokyo","Seol","Madrid"}

sa2 = {"Ohio","Tokyo","Madrid"}

Cities3 = sa1.difference(sa2)

print(Cities3)

sa1 = {"Tokyo","Seol","Madrid"}

sa2 = {"Ohio","Tokyo","Madrid"}

Cities3 = sa1.difference_update(sa2)

print(Cities3)

print(sa1)

set = {"s2","f2"}

set1 = {"s","f"}

print(set.isdisjoint(set1))

cites = {"Kabul","Delhi","AndraPradesh"}

cites2 = {"Kabul","Delhi","AndraPradesh"}

print(cites.issuperset(cites2))

cites = {"Kabul","Delhi","AndraPradesh"}

cites2 = {"Kabul","Delhi","AndraPradesh"}

print(cites.issubset(cites2))

# For Removing cites.remove("AndraPradesh")

# pop for popping a random item

# item = cites.pop( )

# del for delete

# del cites

