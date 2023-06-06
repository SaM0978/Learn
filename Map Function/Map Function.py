def cube(x):
    return x*x*x

print(cube(2))

l = [1,2,3,4,5,6,7,8,9,10]
# newl = []
# for Number in l:
#     newl.append(cube(Number))

newl = list(map(cube, l,'s'))

print(newl)

# FILTER
def Filter_Function(a):
        return a != ['s']
newlnewl = list(filter(Filter_Function, newl))

print(newlnewl)

li = [1,57,4,35,78,3,4]

newk = list(filter(lambda a: a>9,li))

print(newk)

lid = [1,57,45,35,78,36,45]

def f(a):
    if a > 10 and str:
        print("s")


newf = list(filter(f, lid))

# reduce

from functools import reduce

iop = [1,4,7,3,5,92,5]

sum = reduce(lambda x, y: x-y, iop)

print(sum)