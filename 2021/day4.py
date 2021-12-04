with open('day4.txt') as infile:
    boards = []

    nums = infile.readline().strip().split(',')
    nums = [int(num) for num in nums]
    infile.readline()

    j = 0
    s = ''

    for line in infile:
        if j == 5:
            boards.append([int(num) for num in s.split()])
            s = ''
            j = 0
            continue
        s += line
        j += 1

    boards.append([int(num) for num in s.split()])

    noWinner = True
    winners = []

    i = 0

    while noWinner:
        for j, board in enumerate(boards):
            if j in winners:
                continue
            if nums[i] in board:
                idx = board.index(nums[i])
                board[idx] = 'X'

                n = idx % 5
                m = idx // 5
                row = board[m*5:m*5+5]
                column = [board[n + p*5] for p in range(5)]

                if column == ['X']*5 or row == ['X']*5:
                    winner = j
                    boardSum = sum([i if i != 'X' else 0 for i in board])
                    if len(winners) == 0:
                        print(boardSum*nums[i])
                    winners.append(j)
                    if len(winners) == len(boards):
                        print(boardSum*nums[i])
                        noWinner = False
        i += 1
