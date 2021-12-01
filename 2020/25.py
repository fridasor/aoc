def loop(key):
    x = 1; i = 0
    while x != key:
        x = (x*7) % 20201227
        i += 1
    return i

def solve():
    card = 15113849; door = 4206373

    key = 1
    for i in range(loop(card)):
        key = (key*door) % 20201227
    print(key)

solve()
