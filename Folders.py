import os

os.chdir("F:\Samad\Code\Code(Learning)\Python\Learning")

file = 'Automatic Birthday Wisher'
os.mkdir(file)
os.chdir(f"F:\Samad\Code\Code(Learning)\Python\Learning\{file}")
with open(f'{file}.py','w') as w:
    w.write(f'# {file}')