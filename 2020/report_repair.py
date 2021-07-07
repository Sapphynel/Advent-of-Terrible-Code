# Day 1: Report Repair
# Before you leave, the Elves in accounting just need you to fix your
# expense report (your puzzle input); apparently,
# something isn't quite adding up.

# Load
input_list = []

with open("input1.txt", "r") as f:
    for line in f:
        input_list.append(int(line))

input_list.sort()
# Part 1: 2Sum, linear time
start = 0
end = len(input_list) - 1
while start < end:
    first = input_list[start]
    second = input_list[end]
    if (first + second == 2020):
        print("Answer to part 1:", first * second)
        break
    elif (first + second > 2020):
        end -= 1
    else:
        start += 1

# Part 2: 3Sum, Wikipedia version, sums and sorts

for i in range(0, len(input_list) - 2):
    low = input_list[i]
    sweep_start_index = i + 1
    sweep_end_index = len(input_list) - 1
    while (sweep_start_index < sweep_end_index):
        middle = input_list[sweep_start_index]
        high = input_list[sweep_end_index]
        if (low + middle + high == 2020):
            print("Answer to Part 2:", low * middle * high)
            break
        elif (low + middle + high > 2020):
            sweep_end_index -= 1
        else:
            sweep_start_index += 1

print("Finish.")
