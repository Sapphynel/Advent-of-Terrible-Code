# Day 7: Handy Haversacks
# You land at the regional airport in time for your next flight.
# In fact, it looks like you'll even have time to grab some food:
# all flights are currently delayed due to issues in luggage processing.

# Build two graphs: one with edges pointing to contained bags, the other
# with edges pointing to container bags
contained_manifesto = {}
container_manifesto = {}

# stupid wrangle bullshit
with open("input7.txt", "r") as f:
    for line in f:
        bag_container = {}
        # strip the stupid filler
        line = line.replace(" bags", "")
        line = line.replace(" bag", "")
        line = line.replace(" contain", ",")
        line = line.replace(".", "")
        # list the bags...
        bag, bag_list = line[:-1].split(", ")[0], line[:-1].split(", ")[1:]
        # simplify bag_list into a dict
        for element in bag_list:
            bag_rules = element.split(" ", 1)
            # no bags contained case
            if bag_rules[0] == "no":
                pass
            else:
                bag_container[bag_rules[1]] = int(bag_rules[0])
        # dict of dicts, this is hell
        for color in bag_container:
            container_manifesto[bag] = bag_container
            if color in contained_manifesto:
                contained_manifesto[color][bag] = bag_container[color]
            else:
                contained_manifesto[color] = {bag: bag_container[color]}

# Part 1: DFS from "shiny gold"
discovered = []
stack = []
stack.append("shiny gold")
while stack:
    node = stack.pop()
    if node not in contained_manifesto:
        continue
    for edge in contained_manifesto[node].keys():
        if edge not in discovered:
            discovered.append(edge)
            stack.append(edge)
print(len(discovered))


# Part 2: searching, with a twist
count = -1
stack.append("shiny gold")
while stack:
    node = stack.pop()
    count += 1
    if node not in container_manifesto:
        continue
    for edge in container_manifesto[node].keys():
        for i in range(container_manifesto[node][edge]):
            stack.append(edge)
print(count)
