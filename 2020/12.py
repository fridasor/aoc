import numpy as np

def read():
    with open('12d.txt', 'r') as data:
        return [[line[0], int(line[1:-1])] for line in data]

def manh(v):
    x, y = v
    return abs(x) + abs(y)

def change_dir(current_dir, new_dir, val):
    dirs = ['N', 'E', 'S', 'W']
    if new_dir == 'R':
        dirs.reverse()

    return dirs[dirs.index(current_dir) - val//90]

def rotate(v, r, val):
    rotations = {
        'L' : [[0, -1], [1, 0]], #ccw
        'R' : [[0, 1], [-1, 0]]  #cw
        }

    for i in range(val // 90):
        v = np.dot(rotations[r], v)
    return v

def navigate(p=1):
    cmd = read()
    moves = {
        'N' : lambda v, val: v + [0, val],
        'S' : lambda v, val: v - [0, val],
        'E' : lambda v, val: v + [val, 0],
        'W' : lambda v, val: v - [val, 0]
    }

    s = np.array([0, 0])    #ship
    if p == 2: w = np.array([10, 1])    #waypoint
    if p == 1: current_dir = 'E'

    for i in range(len(cmd)):
        c, val = cmd[i]
        if p == 1:
            if c in 'RL':
                current_dir = change_dir(current_dir, c, val)
            elif c == 'F':
                s = moves[current_dir](s, val)
            elif c in 'NSEW':
                s = moves[c](s, val)
        elif p == 2:
            if c in 'NSEW':
                w = moves[c](w, val)
            elif c == 'F':
                s += w*val
            elif c in 'RL':
                w = rotate(w, c, val)

    return manh(s)


print('part 1:', navigate())
print('part 2:', navigate(2))
