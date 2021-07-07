# Day 6: Custom Customs
# As your flight approaches the regional airport where
# you'll switch to a much larger plane, customs declaration forms
# are distributed to the passengers.
groups = 0
with open("inputs/input6.txt", "r") as f:
    people = []
    for line in f:
        if line == "\n":
            print(people[0].intersection(*people[1:]))
            groups += len(people[0].intersection(*people[1:]))
            people = []
            continue
        else:
            person = set()
            for char in line[:-1]:
                person.add(char)
            people.append(person)
            # part 1
            # group.add(char)
    print(people)
    groups += len(people[0].intersection(*people[1:]))

print("Sum of groups:", groups)
