from math import sqrt as squareroot

def double(x):
    return x*2
print(double(5))

cube = lambda x: x*x*x

square_root = lambda x: squareroot(x)

avg = lambda x,y,z: (x+y+z)/2

def appl(fx,value):
    return 6 + fx(value)


def sq(fx,value):
    return 10 - fx(value)



print(cube(9))
print(square_root(81))
print(avg(3,6,10))
print(appl(cube,2))
print(sq(square_root,1010))



