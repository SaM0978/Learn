# Reccursion

# 7 = 7 * 6 * 5 * 4 * 3 * 2 * 1 

# 6 = 6 * 5 * 4 * 3 * 2 * 1

# 5 = 5 * 4 * 3 * 2 * 1

# 4 = 4 * 3 * 2 * 1

# 3 = 3 * 2 * 1

# 2 = 2 * 1

# 1 = 2 * 1

# 0 = 1

def factorial(n):
     if(n==0 or n==1):
         return 1
     else:
         return n * factorial(n-1)

print(factorial(15))

print(factorial(5))

print(factorial(10))

f0 = 0

f1 = 1

f2 = f1 + f0

#fn = f(n - 1) + f(n - 2)

def Fibbonachi_Sequence(n):
    if n == 0:
       print(0)
    elif(n==1):
        print(1)
    else:
        print((n-1)+(n-2))

Fibbonachi_Sequence(7)




