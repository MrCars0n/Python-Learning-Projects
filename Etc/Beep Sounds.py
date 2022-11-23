# Carson Kramer
# Sounds in Python
# 10/3/18
# Period 9

from winsound import *
from random import *

# Beep(frequency, duration)
# frequency is a number from 37 (low pitched) to 32767 (high pitch)
# duration is in milliseconds (1000 is one second)

for n in range(10):
    d1 = int(random() * 6) + 1
    d2 = int(random() * 6) + 1
    total = d1 + d2
    print(d1, d2, total)
    freq = int(random() * 1000) + 37
    Beep(freq, 250)

for freq in range(2000,100,-100):
    Beep(freq, 250)
print("BOOM!")

for freq in range(12000, 25000, 1000):
    Beep(freq, 1000)
