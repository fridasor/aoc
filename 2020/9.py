
def read():
    with open('9d.txt', 'r') as data:
        return [int(line[:-1]) for line in data]

def find():
    nums = read()
    p = 25  #preamble

    for i in range(p, len(nums)):
        s = nums[i-p:i] #previous 25 numbers
        found = False

        for k in range(len(s)):
            for m in range(len(s)):
                if s[m] == s[k]: continue   #skip when equal
                elif s[m] + s[k] == nums[i]:
                    found = True

        if not found: break

    return nums[i]  #number that is not a sum from preamble

def findCont(n):
    nums = read()

    for i in range(len(nums)):
        if nums[i] > n: continue    #ignore numbers > n
        k = i + 1
        reached = False

        while not reached:
            s = sum(nums[i:k])
            if s > n:   #sum is > n
                reached = True
            elif s == n:
                contSet = nums[i:k]
                minmax = (min(contSet) + max(contSet))
                print(f'reached {n}. min + max =', minmax)

                return contSet, minmax
            else:
                k += 1


print(find())       #problem 1
findCont(find())    #problem 2
