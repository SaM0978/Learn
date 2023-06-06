from math import sqrt as root

a = True

print(a := False)

def square_root(sq):
    return root(sq)

print(a := square_root(9))

number = [1,2,3,4,5]

while(n := len(number)) > 0:
    print(number.pop())