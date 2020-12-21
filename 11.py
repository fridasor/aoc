import numpy as np

# i've been debugging this problem for days, but this morning
# i discovered i've misread the problem all along!!!:D

def read():
    with open('11d.txt', 'r') as data:
        l = [list(line.strip()) for line in data.readlines()]
        return np.array(l)

def neighbors(s, i_row, k_col, p = 1):

    adj = [(1, -1), (1, 0), (1, 1), (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1)]
    seats = []
    if p == 2:
        for i, k in adj:
            looking = True
            n = 1

            while looking:
                try:
                    if (i_row + n*i) < 0 or (k_col + n*k) < 0:
                        looking = False
                        break

                    adj_seat = s[i_row + n*i][k_col + n*k]

                    if adj_seat != '.':
                        seats += adj_seat
                        looking = False

                except IndexError:
                    break
                n += 1

    else:
        for i, k in adj:
            try:
                if (i_row + i) == -1 or (k_col + k) == -1:
                    continue
                seats += s[i_row + i][k_col + k]
            except IndexError:
                continue

    return seats


def solve(p = 1, s = read()):
    if p == 2: limit = 5
    else: limit = 4

    s_ = np.full(np.shape(s), '.')  #new seating arrangement

    for i, row in enumerate(s):
        for k, col in enumerate(row):

            if col == '.': continue

            c = neighbors(s, i, k, p)
            n = c.count('#')

            if col == 'L' and n == 0:
                s_[i][k] = '#'
            elif col == '#' and n >= limit:
                s_[i][k] = 'L'
            else:
                s_[i][k] = col

    # check if eq to previous seating:
    eq = s == s_
    all_eq = eq.all()
    return s_, not all_eq

def repeat(p = 1):

    s, changed = solve(p)
    i = 1   #no. of repeats

    while changed:
        s, changed = solve(p, s)
        i += 1
        #print(i)

    if not changed:
        unique, counts = np.unique(s, return_counts=True)
        for i, k in zip(unique, counts): print(i, ':', k)

print('part 1')
repeat()

print('part 2')
repeat(2)
