input = open("input.txt").read().strip().split("\n")

# print(input)

direction = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0,-1)}

def HeadMove(moves):
    HeadPosition = [(0, 0)]
    for i in moves:
        a, b = i.split()
        x, y = direction[a]
        for _ in range(int(b)):
            HeadPosition.append((HeadPosition[-1][0] + x, HeadPosition[-1][1] + y))
    return HeadPosition

print(HeadMove(input))