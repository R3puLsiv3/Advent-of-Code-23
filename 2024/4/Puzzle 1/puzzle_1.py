
def find_word(lines, char, i, j):
    directions = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
    occurrences = 0
    for (h, v) in directions:
        if lines[i + h][j + v] == "M" and lines[i + 2*h][j + 2*v] == "A" and lines[i + 3*h][j + 3*v] == "S":
            occurrences += 1
    return occurrences

def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.split("\n")
    length = len(lines[0])
    padding = 3
    # Add padding so it's not necessary to check for boundaries later.
    lines = ["." * (length + 2 * padding)] * padding + ["." * padding + line + "." * padding for line in lines] + ["." * (length + 2 * padding)] * padding

    result = sum([find_word(lines, char, i, j) for i, line in enumerate(lines) for j, char in enumerate(line) if char == "X"])
    print(result)

if __name__ == '__main__':
    main()
