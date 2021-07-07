# Day 12: Rain Risk

# Your ferry made decent progress toward the island, but the
# storm came in faster than anyone expected. The ferry needs
# to take evasive actions!

# Compass operates by NESW parameters
compass = {270: "N", 0: "E", 90: "S", 180: "W"}
rotation = {"L": -1, "R": 1}
instructions = []
position = [0, 0]
waypoint_position = [10,1]

with open("input12.txt", "r") as f:
    for line in f:
        instructions.append([line[0], int(line[1:])])
# part 1: cartesian
"""
for command in instructions:
    if command[0] in compass.values():
        if command[0] == "N":
            position[1] += command[1]
        elif command[0] == "S":
            position[1] -= command[1]
        elif command[0] == "E":
            position[0] += command[1]
        elif command[0] == "W":
            position[0] -= command[1]
    elif command[0] == "F":
        direction = compass[position[2]]
        if direction == "N":
            position[1] += command[1]
        elif direction == "S":
            position[1] -= command[1]
        elif direction == "E":
            position[0] += command[1]
        elif direction == "W":
            position[0] -= command[1]
    else:
        position[2] = (position[2] + (rotation[command[0]] * command[1])) % 360

    print(position)

print("Final position:", position)
"""
# Part 2: Rotation Shenanigans
for command in instructions:
    if command[0] in compass.values():
        if command[0] == "N":
            waypoint_position[1] += command[1]
        elif command[0] == "S":
            waypoint_position[1] -= command[1]
        elif command[0] == "E":
            waypoint_position[0] += command[1]
        elif command[0] == "W":
            waypoint_position[0] -= command[1]
    elif command[0] != "F":
        if command[0] == "L":
            while command[1] > 0:
                waypoint_position = [-1 * waypoint_position[1], waypoint_position[0]]
                command[1] -= 90
        elif command[0] == "R":
            while command[1] > 0:
                waypoint_position = [waypoint_position[1], -1 * waypoint_position[0]]
                command[1] -= 90
    else:
        for i in range(command[1]):
            position[0] += waypoint_position[0]
            position[1] += waypoint_position[1]
    print(waypoint_position, position)

print("Final position:", position)
