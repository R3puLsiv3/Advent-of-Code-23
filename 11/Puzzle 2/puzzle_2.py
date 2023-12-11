import numpy as np


def main():
    with open("input.txt") as f:
        data = f.read()

    data = data.replace(".", "0").replace("#", "1")
    lines = data.splitlines()

    unexpanded_universe = [[int(j) for j in list(line)] for line in lines]

    y_offset = {}
    current_offset = 0

    for index, row in enumerate(unexpanded_universe):
        if not any(row):
            y_offset[index] = current_offset
            current_offset += 1000000
        else:
            y_offset[index] = current_offset
            current_offset += 1

    x_offset = {}
    current_offset = 0

    unexpanded_universe = np.array(unexpanded_universe).T.tolist()
    for index, column in enumerate(unexpanded_universe):
        if not any(column):
            x_offset[index] = current_offset
            current_offset += 1000000
        else:
            x_offset[index] = current_offset
            current_offset += 1

    unexpanded_universe = np.array(unexpanded_universe).T.tolist()

    galaxies = []
    for i in range(len(unexpanded_universe)):
        for j in range(len(unexpanded_universe[i])):
            if unexpanded_universe[i][j]:
                galaxies.append((i, j))

    adjusted_galaxies = []
    for galaxy in galaxies:
        adjusted_galaxies.append((y_offset[galaxy[0]], x_offset[galaxy[1]]))

    result = 0
    while adjusted_galaxies:
        current_galaxy = adjusted_galaxies.pop()
        for galaxy in adjusted_galaxies:
            result += abs(current_galaxy[0] - galaxy[0]) + abs(current_galaxy[1] - galaxy[1])

    print(result)


if __name__ == '__main__':
    main()
