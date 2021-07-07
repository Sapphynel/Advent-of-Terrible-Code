# Day 4: Passport Processing
# You arrive at the airport only to realize that you
# grabbed your North Pole Credentials instead of your passport.
passports = []

with open("inputs/input4.txt", "r") as f:
    passport = {}
    for line in f:
        if line == "\n":
            passports.append(passport)
            passport = {}
            continue
        else:
            pairs = line.split()
            attributes = [pair.split(":") for pair in pairs]
            for attribute in attributes:
                passport[attribute[0]] = attribute[1]
    passports.append(passport)

# HACK: CID's optional, and I don't feel like dealing with it lmao
part_1_attr_set_cid = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])
part_1_attr_set = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

# helper function to check validity
def validate(passport):
    # wrangle
    birth_year = int(passport["byr"])
    issue_year = int(passport["iyr"])
    exp_year = int(passport["eyr"])
    height = passport["hgt"]
    hair_color = passport["hcl"]
    eye_color = passport["ecl"]
    pid = passport["pid"]

    # Birth year
    if birth_year < 1920 or birth_year > 2002:
        return False
    # Issue year
    if issue_year < 2010 or issue_year > 2020:
        return False
    # Expiration year
    if exp_year < 2020 or exp_year > 2030:
        return False
    # Height
    if "cm" in height:
        units = int(''.join(char for char in height if char.isdigit()))
        if units < 150 or units > 193:
            return False
    if "in" in height:
        units = int(''.join(char for char in height if char.isdigit()))
        if units < 59 or units > 76:
            return False
    if "cm" not in height and "in" not in height:
        return False
    # Hair color
    valid_chars = "0123456789abcdef"
    if hair_color[0] != "#":
        return False
    for char in hair_color[1:]:
        if char not in valid_chars:
            return False
    # Eye color
    valid_colors = ["amb","blu","brn","gry","grn","hzl","oth"]
    if eye_color not in valid_colors:
        return False
    # PID
    if len(pid) != 9:
        return False
    try:
        int(pid)
    except:
        return False

    return True

count = 0
for passport in passports:
    criteria = set(passport.keys())
    if criteria == part_1_attr_set:
        print("Valid, CID not found")
        if validate(passport):
            print("Fields valid")
            count += 1
        else:
            print("Fields invalid")
            continue
    elif criteria == part_1_attr_set_cid:
        print("Valid, CID found")
        if validate(passport):
            print("Fields valid")
            count += 1
        else:
            print("Fields invalid")
            continue
    else:
        print("Invalid")
        continue

print("Valid passports:", count)
