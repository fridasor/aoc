
def read():
    return [0,8,15,2,12,1,4]

def memory_game(number=2020):
    s = read()
    d = {x: i+1 for i, x in enumerate(s[:-1])}  #number: last spoken

    prev = s[-1]

    for i in range(len(s)+1, number+1):
        if prev not in d:
            d[prev] = i-1
            prev = 0
        else:
            idx = (i-1) - d[prev]
            d[prev] = i-1
            prev = idx
    return prev

print('part 1:', memory_game())
print('part 2:', memory_game(30000000))
