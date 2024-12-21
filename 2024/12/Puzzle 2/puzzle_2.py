import random

def clear_side(lines, outer_layer):
    (row, col), direction = random.choice(list(outer_layer.keys()))
    del outer_layer[(row, col), direction]
    match direction:
        case "TOP" | "BOTTOM":
            left = (row, col - 1), direction
            right = (row, col + 1), direction

            while left in outer_layer or right in outer_layer:
                if left in outer_layer:
                    del outer_layer[left]
                    (row, col), direction = left
                    left = (row, col - 1), direction
                if right in outer_layer:
                    del outer_layer[right]
                    (row, col), direction = right
                    right = (row, col + 1), direction
        case "RIGHT" | "LEFT":
            up = (row - 1, col), direction
            down = (row + 1, col), direction

            while up in outer_layer or down in outer_layer:
                if up in outer_layer:
                    del outer_layer[up]
                    (row, col), direction = up
                    up = (row - 1, col), direction
                if down in outer_layer:
                    del outer_layer[down]
                    (row, col), direction = down
                    down = (row + 1, col), direction

def find_area_and_sides(lines, seen, char, pos):
    outer_layer = {}
    area = 0
    plots = [pos]
    while plots:
        (row, col) = plots.pop()
        if (row, col) in seen:
            continue
        seen[(row, col)] = True
        area += 1

        if lines[row + 1][col] == char:
            plots.append((row + 1, col))
        else:
            outer_layer[((row + 1, col), "BOTTOM")] = True
        if lines[row - 1][col] == char:
            plots.append((row - 1, col))
        else:
            outer_layer[((row - 1, col), "TOP")] = True
        if lines[row][col + 1] == char:
            plots.append((row, col + 1))
        else:
            outer_layer[((row, col + 1), "RIGHT")] = True
        if lines[row][col - 1] == char:
            plots.append((row, col - 1))
        else:
            outer_layer[((row, col - 1), "LEFT")] = True

    sides = 0
    while outer_layer:
        clear_side(lines, outer_layer)
        sides += 1

    return area, sides

def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.split("\n")

    length = len(lines[0])
    padding = 1
    # Add padding so it's not necessary to check for boundaries later.
    lines = ["." * (length + 2 * padding)] * padding + ["." * padding + line + "." * padding for line in lines] + [
        "." * (length + 2 * padding)] * padding

    seen = {}

    result = 0
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != "." and (i, j) not in seen:
                area, sides = find_area_and_sides(lines, seen, char, (i, j))
                result += area * sides

    print(result)

if __name__ == '__main__':
    main()
