# Day 2: Password Philosophy
# Your flight departs in a few days from the coastal airport;
# the easiest way down to the coast from here is via toboggan.

# Load
inputs = []
with open("inputs/input2.txt", "r") as f:
    for line in f:
        # Parse it and add:
        row_input = line.split()
        row_input[0] = [int(x) for x in row_input[0].split("-")]
        row_input[1] = row_input[1][0]
        inputs.append(row_input)

# Part 1: Valid Passwords
count = 0
for input in inputs:
    criteria = input[2].count(input[1])
    if criteria > input[0][1]:
        continue
    if criteria < input[0][0]:
        continue
    count += 1

print("Answer to Part 1:", count)

# Part 2: Different Paradigm
new_count = 0
for input in inputs:
    first, second = False, False
    if input[1] == input[2][input[0][0] - 1]:
        first = True
    if input[1] == input[2][input[0][1] - 1]:
        second = True
    if first ^ second:
        new_count += 1

print("Answer to Part 2:", new_count)
