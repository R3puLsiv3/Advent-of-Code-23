import numpy as np


def main():
    with open("input.txt") as f:
        data = f.read()

    data = data.replace(".", "0").replace("#", "1")
    lines = data.splitlines()

    unexpanded_universe = [[int(j) for j in list(line)] for line in lines]

    y_expanded_universe = []
    for row in unexpanded_universe:
        y_expanded_universe.append(row)
        if not any(row):
            y_expanded_universe.append(row)

    expanded_universe = []
    y_expanded_universe = np.array(y_expanded_universe).T.tolist()
    for column in y_expanded_universe:
        expanded_universe.append(column)
        if not any(column):
            expanded_universe.append(column)

    expanded_universe = np.array(expanded_universe).T.tolist()

    galaxies = []
    for i in range(len(expanded_universe)):
        for j in range(len(expanded_universe[i])):
            if expanded_universe[i][j]:
                galaxies.append((i, j))

    result = 0
    while galaxies:
        current_galaxy = galaxies.pop()
        for galaxy in galaxies:
            result += abs(current_galaxy[0] - galaxy[0]) + abs(current_galaxy[1] - galaxy[1])

    print(result)


if __name__ == '__main__':
    main()
