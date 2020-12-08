def read(withNums = False):
    with open('7d.txt', 'r') as data:
        d = {}

        for line in data:
            if 'no other bags' in line:
                continue

            p = line.split()[0] + ' ' + line.split()[1]
            c = line.split('contain ')[1]

            c = c.replace('.\n', '')
            if ', ' in c: c = c.split(', ')
            if isinstance(c, str):
                c = [c]

            if withNums:
                c = [i.split()[0] + ' ' + i.split()[1] + ' ' + i.split()[2] for i in c]
            else:
                c = [i.split()[1] + ' ' + i.split()[2] for i in c]

            exec(f"d['{p}'] = c")
    return d

def check(d):
    l = []
    s = 0

    for i in d:
        if 'shiny gold' in d[i]:
            l.append(i)

    for i in l:
        for k in d:
            if i in d[k] and k not in l:
                l.append(k)

    for i in l:
        for k in d:
            if i in d[k] and k not in l:
                l.append(k)
    return l

addBags = lambda i : int(i.split()[0])
getBag = lambda i : i.split()[1] + ' ' + i.split()[2]

def buy():
    d = read(withNums = True)
    toCheck = ['1 shiny gold']

    shit = ['1 test']
    s = 0
    while toCheck:
        checking = toCheck.pop()
        bag = getBag(checking)
        n = addBags(checking)
        s += n

        if bag in d:
            for k in d[bag]:
                m = addBags(k)
                k = str(n*m ) + ' ' + getBag(k)

                toCheck.append(k)

        #print(n, checking, bag)
    print(s - 1)

d = read()
print(len(check(d)))

buy()
