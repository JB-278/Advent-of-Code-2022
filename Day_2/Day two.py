#  X Rock = 1
#  Y Paper = 2
#  Z Scizzors = 3

# loss = 0
# draw = 3
# win = 6

##Part 1
## AX = 4 AY = 8 AZ = 3
## BX = 1 BY = 5 BZ = 9
## CX = 7 CY = 2 CZ = 6

##Part 2
## AX = 3 AY = 4 AZ = 8
## BX = 1 BY = 5 BZ = 9
## CX = 2 CY = 6 CZ = 7

input = open("Rock_Paper_Scizzors.txt")

input_formatted = input.read().split("\n")

# Part 1
RPS = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}

def LeFunc(x):
    return RPS[x]

output = [sum(map(LeFunc, input_formatted))]

print(output)

# Part 2
RPStoo = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}

def LeFuncToo(x):
    return RPStoo[x]

outputtoo = [sum(map(LeFuncToo, input_formatted))]

print(outputtoo)