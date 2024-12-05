
def find_pattern(lines, char, i, j):
    letters_1 = {lines[i + 1][j - 1], lines[i - 1][j +1]}
    letters_2 = {lines[i + 1][j + 1], lines[i - 1][j - 1]}
    return 1 if "M" in letters_1 and "S" in letters_1 and "M" in letters_2 and "S" in letters_2 else 0

def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.split("\n")
    length = len(lines[0])
    padding = 2
    # Add padding so it's not necessary to check for boundaries later.
    lines = ["." * (length + 2 * padding)] * padding + ["." * padding + line + "." * padding for line in lines] + ["." * (length + 2 * padding)] * padding

    result = sum([find_pattern(lines, char, i, j) for i, line in enumerate(lines) for j, char in enumerate(line) if char == "A"])
    print(result)

if __name__ == '__main__':
    main()