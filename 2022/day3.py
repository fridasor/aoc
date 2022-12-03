
with open('day3.txt', 'r') as infile:
    s = 0
    s2 = 0
    alph = 'abcdefghijklmnopqrstuvwxyz'
    group = []
    for i, line in enumerate(infile):
        line = line.strip()
        first = line[:int(len(line)/2)]
        second = line[int(len(line)/2):]

        for letter in first:
            if letter in second:
                idx = alph.index(letter.lower())
                s += idx + 1 + 26*letter.isupper()
                break

        if i % 3 == 0:
            group.append([])
        group[int(i//3)].append(line)

    for g in group:
        for letter in g[0]:
            if letter in g[1] and letter in g[2]:
                idx = alph.index(letter.lower())
                s2 += idx + 1 + 26*letter.isupper()
                break

    print(s, s2)
