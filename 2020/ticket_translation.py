# Day 16: Ticket Translation

# As you're walking to yet another connecting flight,
# you realize that one of the legs of your re-routed trip coming
# up is on a high-speed train.
import re

criteria = {}
my_ticket = []
other_tickets = []
raw_intervals = []
matching = {}
with open("input16.txt", "r") as f:
    # parsing this file is...annoying.
    # First part
    line = f.readline() # deal with the stupid beginning line...
    while line != "\n":
        category = line.split(":")[0]
        criteria[category] = []
        intervals = re.findall("\d+[-]\d+", line)
        for interval in intervals:
            interval = [int(x) for x in interval.split("-")]
            raw_intervals.append(interval)
            criteria[category].append(interval)
        line = f.readline()

    # Wrangle first part a bit more
    # Second part
    line = f.readline() # deal with the second header
    my_ticket = [int(x) for x in f.readline()[:-1].split(",")]

    # Third part...
    line = f.readline() # deal with the empty line
    line = f.readline() # deal with the third header
    while line:
        line = f.readline()[:-1]
        if line == "":
            break
        other_tickets.append([int(x) for x in line.split(",")])

# Part 1:
# error_range = 0 <-- this was part of the first answer
failures = []
for i in range(len(other_tickets)):
    ticket = other_tickets[i]
    for value in ticket:
        valid_value = False
        for interval in raw_intervals:
            if value >= interval[0] and value <= interval[1]:
                valid_value = True
                break
        if valid_value == False:
            failures.append(i)
            # error_range += value
            break

valid_tickets = [other_tickets[i] for i in range(len(other_tickets)) if i not in failures]

# Part 2: Get matching fields, then do elimination by hand
for i in range(len(my_ticket)):
    fields = [ticket[i] for ticket in valid_tickets]
    for category in criteria:
        valid = True
        interval1 = criteria[category][0]
        interval2 = criteria[category][1]
        for value in fields:
            if value >= interval1[0] and value <= interval1[1]:
                continue
            elif value >= interval2[0] and value <= interval2[1]:
                continue
            else:
                valid = False
                break
        if valid == True:
            if category not in matching:
                matching[category] = [i]
            else:
                matching[category].append(i)
        else:
            continue

# aaaand read off.
for i in range(len(my_ticket)):
    for category in matching:
        if len(matching[category]) == i:
            print(category, matching[category])

# Answer for input:
departure = [7, 4, 1, 12, 17, 13]
product = 1
for value in [my_ticket[i] for i in departure]:
    product *= value
print(product)
