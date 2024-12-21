
def find_score(lines, trailhead):
    row, col = trailhead[0], trailhead[1]
    current = lines[row][col]
    if current == 9:
        return 1
    elif current == -1:
        return 0

    result = 0
    if lines[row + 1][col] == current + 1:
        result += find_score(lines, (row + 1, col))
    if lines[row - 1][col] == current + 1:
        result += find_score(lines, (row - 1, col))
    if lines[row][col + 1] == current + 1:
        result += find_score(lines, (row, col + 1))
    if lines[row][col - 1] == current + 1:
        result += find_score(lines, (row, col - 1))
    return result

def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.split("\n")

    lines = [list(map(int, line)) for line in lines]

    length = len(lines[0])
    padding = 1
    # Add padding so it's not necessary to check for boundaries later.
    lines = [[-1] * (length + 2 * padding)] * padding + [[-1] * padding + line + [-1] * padding for line in lines] + [
        [-1] * (length + 2 * padding)] * padding

    trailheads = [(i, j) for i, line in enumerate(lines) for j, num in enumerate(line) if num == 0]

    result = 0
    for trailhead in trailheads:
        result += find_score(lines, trailhead)

    print(result)

if __name__ == '__main__':
    main()
