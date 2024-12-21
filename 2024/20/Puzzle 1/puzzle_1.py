
def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.split("\n")

    length = len(lines[0])
    padding = 1
    # Add padding so it's not necessary to check for boundaries later.
    lines = ["#" * (length + 2 * padding)] * padding + ["#" * padding + line + "#" * padding for line in lines] + [
        "#" * (length + 2 * padding)] * padding

    start, end = None, None
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "S":
                start = (i, j)
            elif char == "E":
                end = (i, j)

    path = []
    times = {}
    (row, col) = start
    time = 0
    while (row, col) != end:
        path.append((row, col))
        times[(row, col)] = time
        time += 1
        if lines[row + 1][col] != "#" and (row + 1, col) not in times:
            row += 1
        elif lines[row - 1][col] != "#" and (row - 1, col) not in times:
            row -= 1
        elif lines[row][col + 1]  != "#" and (row, col + 1) not in times:
            col += 1
        elif lines[row][col - 1]  != "#" and (row, col - 1) not in times:
            col -= 1
    path.append((row, col))
    times[(row, col)] = time

    time_saves = {}
    for (row, col) in path:
        cheat_reachable = [(row + i,  col + j) for i in range(-2, 3) for j in range(-2, 3) if abs(i) + abs(j) == 2]
        for reachable_row, reachable_col in cheat_reachable:
            if lines[reachable_row][reachable_col] != "#":
                time_saved = times[(reachable_row, reachable_col)] - times[(row, col)] - 2
                if time_saved > 0:
                    if time_saved in time_saves:
                        time_saves[time_saved] += 1
                    else:
                        time_saves[time_saved] = 1

    print(sum([amount for time, amount in time_saves.items() if time >= 100]))

if __name__ == '__main__':
    main()
