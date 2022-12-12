input = open("input.txt").read().strip()

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


HeadOutput = HeadMove(input.split("\n"))
for _ in range(9):
    Output = TailFollow(HeadOutput)

print(len(set(Output)))

# Part 2
def HeadMove2(moves):
    positions = [(0, 0)]
    for move in moves:
        di, n = move.split()
        dx, dy = direction[di]
        for _ in range(int(n)):
            positions.append((positions[-1][0] + dx, positions[-1][1] + dy))
    
    return positions

def follow_head(positions):
    followed_positions = [(0, 0)]
    kx, ky = 0, 0
    for px, py in positions:
        if abs(px - kx) > 1 or abs(py - ky) > 1:
            kx = kx + ((px > kx) - (kx > px))
            ky = ky + ((py > ky) - (ky > py))
        followed_positions.append((kx, ky))
        
    return followed_positions

h2 = HeadMove2(input.split("\n"))
for _ in range(9):
    h2 = follow_head(h2)
    
print(len(set(h2)))