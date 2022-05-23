import random
import time

a = 0

for a in range(10):
    b = random.randint(0, 15)
    print(b)
    time.sleep(1)
    a += 1
