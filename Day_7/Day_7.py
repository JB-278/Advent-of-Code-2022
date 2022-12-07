# input = open("input.txt").read().strip()

# instructions = [x for x in input.split("\n")]

# Part 1 - attempt one bunned off because I couldn't give the dictionary key the value I wanted
# dirdict = {}
# path = []
# output = 0
# dirMax = 100000
# for i in instructions:
#     x = i.strip().split()
#     if x[1] == "cd":
#         if x[2] == "..":
#             path.pop()
#         else:
#             path.append(x[2])
#     elif x[1] == "ls":
#         continue
#     elif x[0] == "dir":
#         continue
#     else:
#         FileSize = int(x[0])
#         for j in range(0, len(path)+1):
#             dirdict[] = FileSize
           
        # if FileSize <= int(dirMax):
        #     output += FileSize



# print(dirdict)
# The answer is not 48748071 - Forgot to set 100000 limit
# The answer is not 3688975 - I'm checking the wrong variable for 100000 limit, needs to be directory not file

# Part 1 - attempt 2
from collections import defaultdict

with open("input.txt") as input:
    instructions = input.readlines()

Max = 100000
path = []
dirsize = defaultdict(int)

for i in instructions:
    i = i.strip().split()
    match i:
        case ["$", "cd", ".."]:
            path.pop()
        case ["$", "cd", dir]:
            x = f"/{dir if dir != '/' else ''}"   # Don't use "" within ""
            path.append("/".join(path) + x)
        case [FileSize, _] if "$" != FileSize != "dir":
            for dir in path:
                dirsize[dir] += int(FileSize)


output = sum([x for x in dirsize.values() if x <= Max])
print(output)

# Part 2 - Ngl this 

TotalDiskSpace = 70000000
SpaceNeeded = 30000000

SpaceRemaining = SpaceNeeded - (TotalDiskSpace - dirsize["/"])

Output2 = min([x for x in dirsize.values() if x >= SpaceRemaining])
print(Output2)