input = open("input.txt")

input_formatted = input.read().strip().split("\n")

# print(input_formatted)

# Part 1
stacks = [
    list("NWFRZSMD"),
    list("SGQPW"),
    list("CJNFQVRW"),
    list("LDGCPZF"),
    list("SPT"),
    list("LRWFDH"),
    list("CDNZ"),
    list("QJSVFRNW"),
    list("VWZGSMR")
]

# print(stacks)

for line in input_formatted[10:]:
    NotNumbers = line.split(" ")
    Numbers = int(NotNumbers[1])
    MoveFrom = int(NotNumbers[3])-1
    MoveTo = int(NotNumbers[5])-1
    for i in range(Numbers):
        stacks[MoveTo].insert(0,stacks[MoveFrom][0])
        stacks[MoveFrom].pop(0)
for stack in stacks:
    print(stack[0])



# Part 2
for line in input_formatted[10:]:
    NotNumbers = line.split(" ")
    Numbers = int(NotNumbers[1])
    MoveFrom = int(NotNumbers[3])-1
    MoveTo = int(NotNumbers[5])-1
    stacks[MoveTo][0:0] = stacks[MoveFrom][0:Numbers]
    del stacks[MoveFrom][0:Numbers]
for stack in stacks:
    print(stack[0])