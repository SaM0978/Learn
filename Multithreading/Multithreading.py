# Multithreading

import threading
import time

def func(sec):
    print(f"Sleeping For {sec} Seconds")
    time.sleep(sec)

# Normal Code
# func(2)
# func(5)

# TurboFlex Code 
t = time.perf_counter()
t1 = threading.Thread(target=func, args=[3])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])
time2 = time.perf_counter()
if t > time2:
    print(t - time2)
else:
    print(time2 - t)

t1.start()
t2.start()
t3.start()

