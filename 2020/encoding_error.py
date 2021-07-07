# Day 9: Encoding Error
# With your neighbor happily enjoying their video game,
# you turn your attention to an open data port on the little screen
# in the seat in front of you.

cipher_entries = []
window = 25

with open("inputs/input9.txt", "r") as f:
    for line in f:
        cipher_entries.append(int(line))

print(len(cipher_entries))

# Part 1: Weakness finding
def two_sum(list, target):
    targets = []
    for element in list:
        if element in targets:
            return True
        targets.append(target - element)
    return False

for i in range(len(cipher_entries) - window):
    preamble = cipher_entries[i:i + window]
    target = cipher_entries[i + window]
    if two_sum(preamble, target) == False:
        print("Weakness found:", target)
        break

print("Part 1 End. Target: 257342611")

# Part 2: Sliding Window
target = 257342611
least_pointer = 0
most_pointer = 1
current_sum = sum(cipher_entries[least_pointer:most_pointer])
while current_sum != target:
    if current_sum > target:
        least_pointer += 1
    elif current_sum < target:
        most_pointer += 1
    current_sum = sum(cipher_entries[least_pointer:most_pointer])

target_weakness = cipher_entries[least_pointer:most_pointer]
print(min(target_weakness) + max(target_weakness))
