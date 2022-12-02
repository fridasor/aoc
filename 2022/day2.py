with open('day2.txt', 'r') as infile:
    elf = {'A' : 0, 'B' : 1, 'C' : 2}
    you = {'X' : 0, 'Y' : 1, 'Z' : 2}
    score = 0
    score2 = 0

    for line in infile:
        elfs, yours = line.strip().split(' ')
        elfs, yours = elf[elfs], you[yours]
        if elfs == yours:
            score += 3
        elif (yours - 1) % 3 == elfs:
            score += 6

        score += yours + 1

        if yours == 0:
            pass
        elif yours == 1:
            score2 += 3
        elif yours == 2:
            score2 += 6

        score2 += ((elfs + yours - 1) % 3) + 1
    
    print(score)
    print(score2)
