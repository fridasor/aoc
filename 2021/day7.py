import numpy as np

with open('day7.txt') as infile:
    crabs = np.array([int(i) for i in infile.readline().split(',')])

M = np.max(crabs)
m = np.min(crabs)
i = m

while i <= M:
    diff = crabs - np.full((len(crabs)), i)
    diff = abs(diff)
    fuel = sum(diff)
    expensiveFuel = sum( (diff * (diff + 1) / 2) )

    if i == m:
        least = fuel
        expensiveLeast = expensiveFuel

    if fuel < least: least = fuel
    i += 1

    if expensiveFuel < expensiveLeast: expensiveLeast = expensiveFuel
    
print(least)
print(expensiveLeast)
