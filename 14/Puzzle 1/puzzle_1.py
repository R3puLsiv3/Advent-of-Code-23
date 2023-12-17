import numpy as np


def main():
    with open("input.txt") as f:
        data = f.read()

    lines = [list(x) for x in data.splitlines()]

    for n in range(len(lines), 0, -1):
        for i, row in enumerate(lines[1:n]):
            for j, char in enumerate(row):
                if lines[i+1][j] == "O":
                    if lines[i][j] == ".":
                        lines[i+1][j] = "."
                        lines[i][j] = "O"
    lines = np.flip(lines, axis=0)

    result = 0
    for i, row in enumerate(lines):
        for j, char in enumerate(row):
            if char == "O":
                result += i + 1

    print(result)


if __name__ == '__main__':
    main()
