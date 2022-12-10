input = open("input.txt").read().strip().split("\n")

# print(input)
# Part 1
direction = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0,-1)}

def HeadMove(moves):
    HeadPosition = [(0, 0)]
    for i in moves:
        a, b = i.split()
        x, y = direction[a]
        for _ in range(int(b)):
            HeadPosition.append((HeadPosition[-1][0] + x, HeadPosition[-1][1] + y))
    return HeadPosition


def TailFollow(HeadPosition):
    TailPosition = [(0, 0)]
    a, b = 0, 0
    for x, y in HeadPosition:
        if abs(x - a) > 1 or abs(y - b) > 1:
            a = a + ((x > a) - (a > x))
            b = b + ((y > b) - (b > y))
        TailPosition.append((a, b))
    return TailPosition


HeadOutput = HeadMove(input)
for _ in range(9):
    Output = TailFollow(HeadOutput)

print(len(set(Output)))

