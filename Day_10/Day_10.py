with open("input.txt") as f:
    input = [line.rstrip() for line in f]

# Part 1

x = 1
cycle = 1
int_list = []
Noop = False              # Potentially flip to False

for i in input:
    if "noop" in i:
        int_list.append(None)
    else:
        this_inst = i.split(' ')
        int_list.append(int(this_inst[1]))

print(int_list)

Num_of_instructions = len(int_list)
c0 = 0                                  #Needed to keep track of index of int_list
Output = 0
Output2 = ''

while c0 < Num_of_instructions:
    # Part 2 inserted here to save space
    if (cycle - 1) % 40 in range(x-1, x+2):
        Output2 += '#'
    else:
        Output2 += '.'
    
    if Noop:
        x += int_list[c0]
        Noop = False
        c0 += 1
    elif int_list[c0] is None:
        c0 += 1
    else:
        Noop = True 

    cycle += 1

    if (cycle - 20) % 40 == 0:
        Output += cycle * x

print(Output)

for i in [Output2[j:j+40] for j in [x*40 for x in range(0, 6)]]:
    print(i)                                                        # Why did you print Output 2 you fool get better at naming variables