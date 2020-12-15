# didn't know python had built-in binary conversion when i did part 1,
# so made my own conversion func. it is awful

def read():
    with open('14d.txt', 'r') as data:
        return [line.strip().split(' = ') for line in data]

def convert(to, num):
    if to == 'bin':     #conv to binary
        b = []
        while num > 0:
            b.insert(0, str(num % 2))
            num = num // 2
        return "".join(b)
    elif to == 'dec':   #conv to dec
        n = 0
        num = str(num)[::-1]

        for i in range(len(num)):
            n += int(num[i]) * 2**i
        return n

def apply_mask(m, val):
    val = convert('bin', int(val))
    val = str(val)
    val = '0'*(len(m) - len(val)) + val
    val = list(val)

    for i in range(len(m)):
        if m[i] == 'X':
            continue
        else:
            val[i] = m[i]
    return "".join(val)

def docking_1():
    commands = read()

    mem = {}

    for line in commands:
        cmd = line[0]
        val = line[1]

        if cmd == 'mask':
            mask = val
        elif cmd[:3] == 'mem':
            adr = int(cmd[4:-1])

            mem[adr] = apply_mask(mask, val)  ###################

    s = 0
    for i in mem:
        s += convert('dec', mem[i])
    return s

print(docking_1())
