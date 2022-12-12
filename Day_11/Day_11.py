import re
import math

# input = open("input.txt").read().strip()

# print(input)


# 1 hour mark and I'm still trying to parse the instructions in
# Temptation to hard code Starting Items is increasing

# Time to learn about Classes


class Monkey:
    def __init__(self, s):
        lines = s.split("\n")                                                               # Split Monkey
        self.items = list(map(int, re.findall("\d+", lines[1])))                            # Look for digits on line index 1

        if not re.search("\d", lines[2]):                                                   # line index 2 can have digits or no digits so check which it is and split accordingly
            self.op = (lambda x : x * x) if '*' in lines[2] else (lambda x: x + x)
        else:
            y = int(re.findall("\d+", lines[2])[0])
            self.op = (lambda x : x * y) if '*' in lines[2] else (lambda x: x + y)
        
        self.test = int(re.findall("\d+", lines[3])[0])                                     # Get value for the Test
        self.If_true = int(re.findall("\d+", lines[4])[0])                                  # Get value for Monkey if True
        self.If_false = int(re.findall("\d+", lines[5])[0])                                 # Get value for Monkey if false
        self.inspections = 0                                                                # Start this at 0

    def turn(self, monkeys, lcm):
        for item in self.items:                                                             # For each item in items
            self.inspections += 1                                                           # increase the number of inspections
            item = self.op(item)                                                            # Give item value 
            item = item % lcm if lcm else item // 3                                         # Worry level, LCM (lowest common multiple) is for Part 2
            monkeys[self.If_false if item % self.test else self.If_true].items.append(item)      # If true then add item to Monkeys
        self.items = []

def run_sim(monkeys, rounds, lcm):                                                          # running simulation, need monkeys, number of rounds, lcm (part 2)
    for _ in range(rounds):                                                                 # for loop for number of rounds
        for m in monkeys:                                                                   # For each monkey
            m.turn(monkeys, lcm)                                                            # call the turn function

def monkey_business(monkeys):                                                               # This is the output
    x = sorted([m.inspections for m in monkeys], reverse=True)                              # Make list of inspections number for each monkey
    return x[0] * x[1]                                                                      # Multiply as requested

def part1():
    monkeys = [Monkey(s) for s in open("input.txt").read().split("\n\n")]                   # Split Monkeys into each monkey
    run_sim(monkeys, 20, 0)                                                                 # run simulation for 20 rounds with no lcm
    print(monkey_business(monkeys))                                                         # Output

part1()                                                                                     # Call function

def part2():
    monkeys = [Monkey(s) for s in open('input.txt').read().split('\n\n')]
    run_sim(monkeys, 10_000, math.lcm(*[m.test for m in monkeys]))                          # Same again but this time for 10000 rounds and use lcm function for lowest common multiple for the tests involved, no need to go super high
    print(monkey_business(monkeys))

part2()                                                                                     # Call function