input = open("Rucksacks.txt").read().strip().split()


# Part 1
output1 = 0
for line in input:                                                      # loop through each line in txt file
    firsthalf, secondhalf = line[:len(line)//2], line[len(line)//2:]    # Split each string into two parts
    same = (set(firsthalf) & set(secondhalf)).pop()                     # remove letter that appears in both sets
    if same.islower():                                                  # if letter is lower case then add value 
        output1 += ord(same) - ord("a") + 1
    else:                                                               # is letter is upper case then add value
        output1 += ord(same) - ord("A") + 27

print(output1)

# Part 2
output2 = 0
for line in range(0, len(input), 3):
    first, second, third = input[line:line+3]
    same = (set(first) & set(second) & set(third)).pop()
    if same.islower():
        output2 += ord(same) - ord("a") + 1
    else:
        output2 += ord(same) - ord("A") + 27

print(output2)