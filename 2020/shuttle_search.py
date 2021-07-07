# Day 13 - Shuttle Search

# Your ferry can make it safely to a nearby port,
# but it won't get much further.

with open("input13.txt", "r") as f:
    time = int(f.readline())
    bus_timeline = f.readline().strip().split(",")

# Part 1
buses = [int(x) for x in bus_timeline if x != "x"]
minutes = [[x, x - divmod(time, x)[1]] for x in buses]
print("Timeline:", minutes) # read it off, because this dataset's small

# Part 2: Chinese Remainder Theorem
parameters = [list(x) for x in list(enumerate(bus_timeline)) if x[1] != "x"]

for parameter in parameters:
    parameter[1] = int(parameter[1])

def extended_euclidean(mod1, mod2):
    if mod2 == 0:
        return (1, 0)
    (x, y) = extended_euclidean(mod2, mod1 % mod2)
    k = mod1 // mod2
    return [y, x - k * y]

def crt(rem1, mod1, rem2, mod2):
    (x, y) = extended_euclidean(mod1, mod2)
    m = mod1 * mod2
    n = rem2 * x * mod1 + rem1 * y * mod2
    return [(n % m + m) % m, m]

while len(parameters) > 1:
    first = parameters.pop()
    second = parameters.pop()
    new = crt(first[0], first[1], second[0], second[1])
    parameters.append(new)

answer = parameters.pop()
print(answer[1] - answer[0])
