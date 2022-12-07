input = open("Cleaning_Sectors.txt").read().strip().split()


# Part 1
output = 0
for line in input:
    sector1, sector2 = line.split(",")
    FirstElfFloor, FirstElfCeiling = map(int, sector1.split("-"))
    SecondElfFloor, SecondElfCeiling = map(int, sector2.split("-"))
    if FirstElfFloor <= SecondElfFloor and FirstElfCeiling >= SecondElfCeiling or SecondElfFloor <= FirstElfFloor and SecondElfCeiling >= FirstElfCeiling:
        output += 1

print(output)

# Part 2
output2 = 0
for line in input:
    sector1, sector2 = line.split(",")
    FirstElfFloor, FirstElfCeiling = map(int, sector1.split("-"))
    SecondElfFloor, SecondElfCeiling = map(int, sector2.split("-"))
    if FirstElfCeiling >= SecondElfFloor and FirstElfFloor <= SecondElfCeiling or SecondElfCeiling >= FirstElfFloor and SecondElfFloor <= FirstElfCeiling:
        output2 += 1

print(output2)


# Part 1 alternative WIP
output3 = 0
for line in input:
    sectors = line.split(",")
    FirstElf = sectors[0].split("-")
    SecondElf = sectors[1].split("-")
    if (set(FirstElf) & set(SecondElf)):
        output3 += 1

print(output3) # outputting 312, should be 444, don't know why