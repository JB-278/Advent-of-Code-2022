with open("input.txt") as le:
    input = le.read().strip().split()

trees = []
for i in input:
    trees.append(list(map(int, list(i))))
    
    
# print(trees)

# Part 1
def CheckLeft(x, y):
    for i in range(0, y):
        if trees[x][i] >= trees[x][y]:
            return False
    return True

def CheckRight(x, y):
    for i in range(y+1, len(trees[0])):
        if trees[x][i] >= trees[x][y]:
            return False
    return True


def CheckUp(x, y):
    for i in range(0, x):
        if trees[i][y] >= trees[x][y]:
            return False
    return True

def CheckDown(x, y):
    for i in range(x+1, len(trees)):
        if trees[i][y] >= trees[x][y]:
            return False
    return True


output = 0
for x in range(1, len(trees)-1):
    for y in range(1, len(trees[0])-1):
        if CheckLeft(x, y) or CheckRight(x, y) or CheckUp(x, y) or CheckDown(x,y):
            output += 1
output += (len(trees)+len(trees[0])-2)*2

print(output)

# Part 2
def CountLeft(x, y):
    left = 0
    for i in range(y-1, -1, -1):
        if trees[x][i] < trees[x][y]:
            left += 1
        else:
            return left+1
    return left

def CountRight(x, y):
    right = 0
    for i in range(y+1, len(trees[0])):
        if trees[x][i] < trees[x][y]:
            right += 1
        else:
            return right+1
    return right

def CountUp(x, y):
    up = 0
    for i in range(x-1, -1, -1):
        if trees[i][y] < trees[x][y]:
            up += 1
        else:
            return up+1
    return up

def CountDown(x, y):
    down = 0
    for i in range(x+1, len(trees)):
        if trees[i][y] < trees[x][y]:
            down += 1
        else:
            return down+1
    return down

output2 = 0
for x in range(1, len(trees)-1):
    for y in range(1, len(trees[0])-1):
        output2 = max(output2, CountLeft(x, y) * CountRight(x, y) * CountUp(x, y) * CountDown(x, y))

print(output2)