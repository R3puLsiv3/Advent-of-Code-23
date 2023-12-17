import numpy as np


def tilt(lines):
    for n in range(len(lines), 0, -1):
        for i, row in enumerate(lines[1:n]):
            for j, char in enumerate(row):
                if lines[i + 1][j] == "O":
                    if lines[i][j] == ".":
                        lines[i + 1][j] = "."
                        lines[i][j] = "O"
    return lines


def main():
    with open("input.txt") as f:
        data = f.read()

    lines = [list(x) for x in data.splitlines()]
    configurations = {}

    end_index = 0
    while True:
        end_index += 1
        lines = tilt(lines)
        lines = np.rot90(lines, -1)
        lines = tilt(lines)
        lines = np.rot90(lines, -1)
        lines = tilt(lines)
        lines = np.rot90(lines, -1)
        lines = tilt(lines)
        lines = np.rot90(lines, -1)

        key_lines = (tuple([tuple(x) for x in lines]))

        if key_lines in configurations.keys():
            start_index = configurations[key_lines]
            break
        else:
            configurations[key_lines] = end_index

    cycle_range = end_index - start_index
    while (1000000000 - end_index) % cycle_range != 0:
        end_index += 1
        lines = tilt(lines)
        lines = np.rot90(lines, -1)
        lines = tilt(lines)
        lines = np.rot90(lines, -1)
        lines = tilt(lines)
        lines = np.rot90(lines, -1)
        lines = tilt(lines)
        lines = np.rot90(lines, -1)

    lines = np.flip(lines)

    result = 0
    for i, row in enumerate(lines):
        for j, char in enumerate(row):
            if char == "O":
                result += i + 1

    print(result)


if __name__ == '__main__':
    main()
