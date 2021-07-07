# Day 15: Rambunctious Recitation

# You catch the airport shuttle and try to book
# a new flight to your vacation island.

starter_queue = [2, 1, 10, 11, 0, 6]
ages = {2: 1, 1: 2, 10: 3, 11: 4, 0: 5, 6: 6}
# Part 1 & 2
for i in range(len(starter_queue) + 1, 30000001):
    check_number = starter_queue[-1]
    if check_number in ages:
        starter_queue.append(i - 1 - ages[check_number])
        ages[check_number] = i - 1
    else:
        ages[check_number] = i - 1
        starter_queue.append(0)

print(starter_queue[-1])
