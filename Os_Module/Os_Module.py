import os

# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(0,19):
#     os.mkdir(f"Python/Learning/Code with harry{i+1}")

# chutney wali phat mirche

# folders = os.listdir("data")

# print(folders)

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))

# Python program to explain os.getcwd() method
		
# importing os module
import os
	
# Get the current working
# directory (CWD)
cwd = os.getcwd()

	
# Print the current working
# directory (CWD)
print("Current working directory:", cwd)

os.chdir("Python/Learning")
 
OP = os.getcwd()

print(OP)

l = os.listdir("Code with harry")

print(l)

for files in l:
    print("1")
    os.mkdir(f"{files}")
