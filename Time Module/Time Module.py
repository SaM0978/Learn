import time

init = time.time() # Stop Watch

for i in range(100):
    print(i)

print(time.time()-init) # Minus 

# time.sleep(4) # Python Waits

print(34)

t = time.localtime()

formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)