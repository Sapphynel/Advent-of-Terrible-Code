# Day 8: Handheld Halting
# Your flight to the major airline hub reaches cruising altitude
# without incident. While you consider checking the in-flight menu
# for one of those drinks that come with a little umbrella,
# you are interrupted by the kid sitting next to you.
acc_points = []
possible_problem_nop = []
possible_problem_jmp = []

with open("inputs/input8.txt", "r") as f:
    pointer = -1
    for line in f:
        pointer += 1
        instruction = []
        parse = line.split(" ")
        if parse[0] == "nop":
            if parse[1][0] == "+":
                instruction = [0, 1, int(parse[1][1:])]
            else:
                instruction = [0, 1, -1 * int(parse[1][1:])]
            possible_problem_nop.append(pointer)
        elif parse[0] == "acc":
            if parse[1][0] == "+":
                instruction = [int(parse[1][1:]), 1]
            else:
                instruction = [-1 * int(parse[1][1:]), 1]
        elif parse[0] == "jmp":
            if parse[1][0] == "+":
                instruction = [0, int(parse[1][1:])]
            else:
                instruction = [0, -1 * int(parse[1][1:])]
            possible_problem_jmp.append(pointer)
        acc_points.append(instruction)

print(acc_points[363])

# Part 1: run the code
def run_code(instructions):
    seen = []
    acc = 0
    pointer = 0
    while pointer not in seen:
        seen.append(pointer)
        acc += instructions[pointer][0]
        pointer += instructions[pointer][1]
        if pointer == len(instructions):
            print("Success!", acc)
            break

run_code(acc_points)

# Part 2: try for possible problems
for problem_index in possible_problem_nop:
    fixed_instructions = [instruction for instruction in acc_points]
    fixed_instructions[problem_index] = [0, fixed_instructions[problem_index][2]]
    run_code(fixed_instructions)

for problem_index in possible_problem_jmp:
    fixed_instructions = [instruction for instruction in acc_points]
    fixed_instructions[problem_index] = [0, 1]
    run_code(fixed_instructions)
