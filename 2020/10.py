from functools import lru_cache
from timeit import repeat

def read():
    with open('10d.txt', 'r') as data:
        l = [0] + [int(line[:-1]) for line in data]
        l.sort()
        return l

def jolt_diffs():
    one, three = 0, 0
    a = read()
    a.insert(0, 0)  #remember charging outlet, 0 jolts

    for i in range(len(a) - 1):
        diff = a[i+1] - a[i]

        if diff == 1: one += 1
        elif diff == 3: three += 1

    return one * (three+1)  #remember built-in adapter

#i would like to thank realpython.com for saving my ass on this one.
#https://realpython.com/lru-cache-python/#unpacking-the-functionality-of-lru_cache

M = max(read())
@lru_cache(None)

def paths(i=M, a=read()):
    p = 0   #number of path arrangements

    if i == 0:
        return 1    #one possible path from outlet to first adapter

    next = [(i - n) for n in (1, 2, 3) if (i - n) in a] #next adapters
    for k in next:
        p += paths(k)
    return p

print('product of 1-jolt-diffs and 3-jolt-diffs:', jolt_diffs())
print('possible paths to device:', paths())
