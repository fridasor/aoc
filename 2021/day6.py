import numpy as np

with open('day6.txt', 'r') as infile:
    fish0 = [int(f) for f in infile.readline().split(',')]

timers = np.zeros(9)
for i in fish0: timers[i] += 1

T = 80
T = 256
i = 0

A = np.zeros((9, 9))
for k in range(8): A[k, k+1] = 1

while i < T:
    i += 1

    day0 = timers[0]
    timers = A.dot(timers)
    timers[6] += day0
    timers[8] = day0

print(sum(timers))
