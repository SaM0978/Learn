import random

# Generate a random float
x = random.random()
print(x)

# Generate a random integer
y = random.randint(1, 10)
print(y)

# Choose a random element from a list
my_list = ["apple", "banana", "cherry"]
z = random.choice(my_list)
print(z)

# Shuffle a list
random.shuffle(my_list)
print(my_list)

# Sample elements from a list
my_list = [1, 2, 3, 4, 5]
sample = random.sample(my_list, 3)
print(sample)
