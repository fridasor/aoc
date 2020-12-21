from itertools import chain
from functools import reduce

def read():
    with open('16d.txt', 'r') as data:
        r = {}
        for l in data:
            if l == '\n': break

            l = l.strip().split(': ')
            r[l[0]] = [list(map(int, i.split('-'))) for i in l[1].split(' or ')]

        data.readline()
        yours = [int(i) for i in data.readline().strip().split(',')]

        data.readline(); data.readline()

        others = [list(map(int, l.strip().split(','))) for l in data]
        return r, yours, others


def scan():
    rules, _, others = read()

    rate = 0
    valid_t = []

    for t in others:
        valid = 0
        for i, n in enumerate(t):

            valid_n = False

            for r in chain.from_iterable(rules.values()):
                if n in range(r[0], r[1] + 1):
                    valid_n = True
                    valid += 1
                    break

            if not valid_n:
                rate += n

        if valid == len(t):
            valid_t.append(t)

    print(rate)
    return rules, _, valid_t

def check(r, t):
    valids = [1]*len(t[0])

    for ticket in t:
        for i, n in enumerate(ticket):
            if n in range(r[0][0], r[0][1]+1) or n in range(r[1][0], r[1][1]+1):
                valids[i] *= 1
            else:
                valids[i] *= 0

    return valids

def determine():
    r, ticket, t = scan()

    r = {i : r[i] for (i) in r if i.startswith('de')}

    for rule in r:
        r[rule] = check(r[rule], t)

    for i in r: print(r[i], '\t', i)

    prod = reduce(lambda x, y : x*y, [ticket[i] for i in (-3, -5, 2, -1, 6)])

    for i in (79, 101, 139, 97, 83, 181, 89):
        print(f'{prod} * {i} \t{prod*i}')

determine()
