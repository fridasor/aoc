def read():
    with open('8d.txt', 'r') as data:
        steps = [line[:-1].split() for line in data]

    steps = list(map(lambda x : [x[0], int(x[1])], steps))
    return steps

def advance(step, i, a):
    if step[0] == 'jmp':
        i += step[1]
    elif step[0] == 'acc':
        i += 1
        a += step[1]
    elif step[0] =='nop':
        i += 1
    return i, a

def run(s):
    i = 0
    a = 0
    unfinished = True

    while unfinished:
        step = s[i]

        if s[i] == '-': unfinished = False  #if entering a loop
        else: s[i] = '-'

        i, a = advance(step, i, a)

        if i+1 >= len(s):
            print('loop avoided, a =', a)
            unfinished = False

    return a

def find(s):    #find jmps and nops
    nops, jmps = [], []

    for i in range(len(s)):
        if s[i][0] == 'jmp': jmps.append(i)
        elif s[i][0] == 'nop': nops.append(i)

    return nops, jmps

def changeThenRun(steps):
    nops, jmps = find(steps)

    for i in nops:
        s = list(steps)

        s[i] = ['jmp', s[i][1]]
        run(s)

    for i in jmps:
        s = list(steps)
        s[i] = ['nop', s[i][1]]
        run(s)

steps = read()          #problem 1
prob_1 = run(steps)
print(prob_1)
changeThenRun(read())   #problem 2
