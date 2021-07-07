# Day 14: Docking Data

# As your ferry approaches the sea port,
# the captain asks for your help again. The computer
# system that runs this port isn't compatible with the docking
# program on the ferry, so the docking parameters aren't being
# correctly initialized in the docking program's memory.
import re, itertools

addresses = {}
current_mask = ""
writes = []

with open("inputs/input14.txt", "r") as f:
    for line in f:
        if "mask" in line:
            current_mask = line[7:-1]
        else:
            entry = [int(x) for x in re.findall("\d+", line)]
            # addresses[entry[0]] = [list(str(bin(entry[1]))[2:].zfill(36)), list(current_mask)]
            writes.append([list(str(bin(entry[0]))[2:].zfill(36)), list(current_mask), entry[1]])

# part 1
# for address in addresses:
#     for i in range(36):
#         if addresses[address][1][i] != "X":
#             addresses[address][0][i] = addresses[address][1][i]
# sum = 0
# for address in addresses:
#     addresses[address] = ["".join(x) for x in addresses[address]]
#     sum += int(addresses[address][0], 2)
# print

# part 2
for write in writes:
    for i in range(36):
        if write[1][i] == "1":
            write[0][i] = write[1][i]
        elif write[1][i] == "X":
            write[0][i] = "%s"
        else:
            continue
    write[0] = "".join(write[0])
    binary_strings = list([i for i in itertools.product([0, 1], repeat=write[0].count("%s"))])
    for binary_string in binary_strings:
        address = write[0] % (binary_string)
        addresses[address] = write[2]

print(sum(addresses.values()))
