input = open("input.txt").read()


# Part 1

def LeFunc():
    for i in range(0, len(input)):
        output = input[i : i + 4]
        if len(output) == len(set(output)):
            return i + 4

print(LeFunc())

# Part 2

def LeFuncToo():
    for i in range(0, len(input)):
        output = input[i : i + 14]
        if len(output) == len(set(output)):
            return i + 14

print(LeFuncToo())