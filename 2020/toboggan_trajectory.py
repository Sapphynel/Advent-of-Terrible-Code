# Day 3: Toboggan Trajectory
# With the toboggan login problems resolved, you set off toward the airport.
# While travel by toboggan might be easy, it's certainly not safe:
# there's very minimal steering and the area is covered in trees.
trees = []
period = 0
# Load
with open("inputs/input3.txt", "r") as f:
    period = len(f.readline()) - 1
    f.seek(0,0)
    for line in f:
        row_trees = []
        for i in range(len(line)):
            if line[i] == "#":
                row_trees.append(i)
        trees.append(row_trees)

# Part 1: Fixed slope --> mod to given slope, either using the range or
# by multiplying the i
hits = 0
for i in range(0, len(trees)):
    current_position = (3 * i) % period
    if current_position in trees[i]:
        hits += 1

print("Hits with given slope:", hits)

# 47, 195, 84, 70, 70
