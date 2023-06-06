import os

g =  os.getcwd()

print(g)

c = os.chdir("Python/Learning/Code with harry/File IO")

print(c)
print(g)

s = os.getcwd()

print(s)

# f = open("myfile.txt",'r')

# print(f)

# G = f.read()

# print(G)

# f.close()

# f = open("Hussain.txt",'w')

# print(f)

# G = f.write("Samad")

# print(G)

# f.close()

# Append

# f = open("Hussain.txt",'a')

# print(f)

# H = f.write(" Gussain")

# f.close()

# Read Binary

# f = open("Hussain.txt",'rb')

# print(f)

# f.close()


with open("Hussain.txt","a") as f:
    f.write("Hey I Am Inside This File: ")