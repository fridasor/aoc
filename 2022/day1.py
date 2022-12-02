with open('day1.txt', 'r') as infile:
    cals = []
    s = 0
    for line in infile:
        if line == '\n':
            cals.append(s)
            s = 0
        else:
            s += int(line)
    cals.append(s)
    print(max(cals))

    cals.sort()
    print(sum(cals[-3:]))
