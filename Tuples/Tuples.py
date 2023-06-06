f = (4,6,"fa","Tuple","Hussain Bhai Cooker","!")

print(type(f), "\n", f)

if 2 in f:
 print("S") 

if 5 and 75 not in f:
 print("5 and 75 is not there") 

tup2 = f[0:5]

print(tup2)

tuple1 = ("!","$","%","!","&")

res = tuple1 and f.count("!")

print("Your Tuple Count ",res)

index = tuple1.index("%")

print(index)

