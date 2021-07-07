# Day 10: Adapter Array
# Patched into the aircraft's data port, you discover weather
# forecasts of a massive tropical storm. Before you can
# figure out whether it will impact your vacation plans,
# however, your device suddenly turns off!
adapters = [0]

with open("input10.txt", "r") as f:
    for line in f:
        adapters.append(int(line))

# sort adapters
adapters.sort()
# Add device
adapters.append(adapters[-1] + 3)

print(adapters)
# Part 1
one_diff = 0
three_diff = 0
for i in range(1, len(adapters)):
    diff = adapters[i] - adapters[i - 1]
    if diff == 1:
        one_diff += 1
    elif diff == 3:
        three_diff += 1

# Part 2: Dynamic Programming (Triple Fibonacci)
results = [1, 1, 2]
for i in range(3, adapters[-1] + 1):
    if i in adapters:
        results.append(results[i-1] + results[i-2] + results[i-3])
    else:
        results.append(0)

print(results[-1])
