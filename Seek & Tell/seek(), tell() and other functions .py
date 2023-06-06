import os

os.chdir("Python\Learning\Code with harry\Seek & Tell")

# with open("sample.txt","a") as g:
#     g.write(" Hussain Bhai Cooker")

# with open("sample.txt", "r") as f:
#     print(type(f))
#     # Move to the 10th byte in the file
#     f.seek(15)
#     # Read the next 5 bytes
#     print(f.tell())
#     data = f.read(5)
#     print(data)

with open ("sample.txt","w") as f:
        f.write("Hello World3!")
        f.truncate(2)