with open('day10.txt') as infile:
    d = {
        '[' : ']',
        '(' : ')',
        '<' : '>',
        '{' : '}'
    }

    points = {
        ')' : [3, 1],
        ']' : [57, 2],
        '}' : [1197, 3],
        '>' : [25137, 4]
    }

    error = 0
    scores = []
    for line in infile:
        corrupted = False
        openString = ''
        closeString = ''

        for symbol in line.strip():
            if symbol in d.keys():
                openString += symbol
                closeString = d[symbol] + closeString
            else:
                if closeString[0] == symbol:
                    closeString = closeString[1:]
                    openString = openString[:-1]
                elif symbol == '\n':
                    continue
                elif symbol != '\n':
                    found = symbol
                    error += points[found][0]
                    corrupted = True
                    break
        if not corrupted:
            score = 0
            for symbol in closeString:
                score *= 5
                score += points[symbol][1]
            scores.append(score)

print(error)
scores.sort()
print(scores[(len(scores)//2)])
