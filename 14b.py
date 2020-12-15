from itertools import product

def read():
    with open('14d.txt', 'r') as data:
        return [line.strip().split(' = ') for line in data]

def apply_mask_adr(m, a):
    a = list(a)
    a = ['0']*(len(m) - len(a)) + a
    idx = []

    for i in range(len(m)):
        if m[i] == 'X':
            a[i] = 'X'
            idx.append(i)
        elif m[i] == '1':
            a[i] = '1'

    comb = []
    for i in product(['0', '1'], repeat=len(idx)):
        c = a.copy()
        for k, x in enumerate(idx):
            c[x] = i[k]

        comb.append(c)
    return ["".join(i) for i in comb]

def docking_2():
    commands = read()

    mem = {}

    for line in commands:

        c = line[0]
        val = line[1]

        if c == 'mask':
            mask = val
        else:
            adr = line[0][4:-1]
            adr = bin(int(adr))
            adr = str(adr)[2:]
            adr = apply_mask_adr(mask, adr)
            for i in adr:
                mem[i] = val

    return sum(int(mem[i]) for i in mem)

s = docking_2()
print(s)
