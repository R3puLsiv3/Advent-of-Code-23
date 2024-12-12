
def find_area_and_perimeter(lines, seen, char, pos):
    perimeter = 0
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
            perimeter += 1
        if lines[row - 1][col] == char:
            plots.append((row - 1, col))
        else:
            perimeter += 1
        if lines[row][col + 1] == char:
            plots.append((row, col + 1))
        else:
            perimeter += 1
        if lines[row][col - 1] == char:
            plots.append((row, col - 1))
        else:
            perimeter += 1

    return area, perimeter

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
                area, perimeter = find_area_and_perimeter(lines, seen, char, (i, j))
                result += area * perimeter

    print(result)

if __name__ == '__main__':
    main()
