# Day 11 - Seating System
# Your plane lands with plenty of time to spare.
# The final leg of your journey is a ferry that goes
# directly to the tropical island where you can finally start your vacation.
import copy
first_grid = []
with open("inputs/input11.txt", "r") as f:
    row = []
    for line in f:
        for char in line[:-1]:
            row.append(char)
        first_grid.append(row)
        row = []

second_grid = copy.deepcopy(first_grid)

def step(grid, new_grid):
    # parameters
    width = len(grid[0])
    height = len(grid)
    # For each entry...
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            top, bottom, left, right = False, False, False, False
            if grid[row][col] == ".":
                continue
            # bound check
            if row == 0:
                top = True
            if row == len(grid) - 1:
                bottom = True
            if col == 0:
                left = True
            if col == len(grid[0]) - 1:
                right = True
            tags = [top, bottom, left, right]
            count = check(grid, row, col, tags)
            if grid[row][col] == "L" and count == 0:
                new_grid[row][col] = "#"
            elif grid[row][col] == "#" and count >= 6:
                new_grid[row][col] = "L"

def check(grid, row, col, tags):
    # part 2 needs these parameters god why
    width = len(grid[0])
    height = len(grid)
    length = 1
    count = 0
    hor = [-1, 0, 1]
    vert = [-1, 0, 1]
    if tags[0] == True:
        vert.pop(0)
    if tags[1] == True:
        vert.pop()
    if tags[2] == True:
        hor.pop(0)
    if tags[3] == True:
        hor.pop()
    for hor_move in hor:
        for vert_move in vert:
            if grid[row + vert_move][col + hor_move] == "#":
                count += 1
            elif grid[row + vert_move][col + hor_move] == ".":
                current_row = row + vert_move
                current_col = col + hor_move
                while grid[current_row][current_col] == ".":
                    current_row += vert_move
                    current_col += hor_move
                    # bound check
                    if current_row == -1 or current_row == len(grid) or current_col == -1 or current_col == len(grid[0]):
                        break
                if current_row == -1 or current_row == len(grid) or current_col == -1 or current_col == len(grid[0]):
                    continue
                if grid[current_row][current_col] == "#":
                    count += 1
    return count

step(first_grid, second_grid)

while first_grid != second_grid:
    first_grid = copy.deepcopy(second_grid)
    step(first_grid, second_grid)

count = 0
for row in second_grid:
    count += row.count("#")

print(count)
