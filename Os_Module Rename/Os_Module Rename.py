import os

if(not os.path.exists("data")):
    os.mkdir("data")

for i in range(1,8):
    os.rename(f"data/Day{i}", f"data/Hussain{i}"  )


