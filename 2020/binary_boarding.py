# Day 5: Binary Boarding
# You board your plane only to discover a new problem:
# you dropped your boarding pass!

binary_check = {"F": "0", "B": "1", "L": "0", "R": "1"}

seats = []

with open("inputs/input5.txt", "r") as f:
    for line in f:
        string_id = ''.join([binary_check[char] for char in line.strip()])
        split = [int(string_id[0:7], 2), int(string_id[7:], 2)]
        seats.append(split)

seat_ids = []

# Part 1: Seat ID
max_id = 0
for seat in seats:
    id = 8 * seat[0] + seat[1]
    if id > max_id:
        max_id = id
    seat_ids.append(id)

print("Max ID is:", max_id)

# Part 2: sort and search
seat_ids.sort()
start = seat_ids[0]
while True:
    if start + 1 not in seat_ids:
        print(start + 1)
        break
    else:
        start += 1
