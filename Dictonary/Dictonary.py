# Dictonary

info = {
    "Samad": "Human Being",
    "Spoon": "Object",
    777: "Hussain",
    "Name": "Zeenat"
}
  
print(info[777])

print(info.get("Name"))

print(info.keys())

print(info.values())

print(info.items())

for key, value in info.items():
    print(f'The Value in Corresponding To The Key {key} is {info[key]}')

ep = {122:45, 123:89, 567: 69, 670: 66}

ep2 = {222:67, 454:69, 777:5}

ep3 = ep.update(ep2)

print(ep)

pop = ep.pop(222)

print("Sam" , ep.popitem())

print(pop)

print(ep)






























































