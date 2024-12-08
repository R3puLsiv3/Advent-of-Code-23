import itertools


def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.split("\n")
    height = len(lines)
    length = len(lines[0])

    antennas = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != ".":
                if char not in antennas:
                    antennas[char] = [(i, j)]
                else:
                    antennas[char].append((i, j))

    antinodes = set()
    for key in antennas:
        for ((row1, col1), (row2, col2)) in itertools.combinations(antennas[key], 2):
                dist_vertical = abs(row1 - row2)
                dist_horizontal = abs(col1 - col2)

                if row1 <= row2 and col1 <= col2:
                    antinode_row1 = row1 - dist_vertical
                    antinode_row2 = row2 + dist_vertical
                    antinode_col1 = col1 - dist_horizontal
                    antinode_col2 = col2 + dist_horizontal
                elif row1 <= row2 and col1 >= col2:
                    antinode_row1 = row1 - dist_vertical
                    antinode_row2 = row2 + dist_vertical
                    antinode_col1 = col1 + dist_horizontal
                    antinode_col2 = col2 - dist_horizontal
                elif row1 >= row2 and col1 <= col2:
                    antinode_row1 = row1 + dist_vertical
                    antinode_row2 = row2 - dist_vertical
                    antinode_col1 = col1 - dist_horizontal
                    antinode_col2 = col2 + dist_horizontal
                else:
                    antinode_row1 = row1 + dist_vertical
                    antinode_row2 = row2 - dist_vertical
                    antinode_col1 = col1 + dist_horizontal
                    antinode_col2 = col2 - dist_horizontal

                if 0 <= antinode_row1 < height and 0 <= antinode_col1 < length:
                    antinodes.add((antinode_row1, antinode_col1))
                if 0 <= antinode_row2 < height and 0 <= antinode_col2 < length:
                    antinodes.add((antinode_row2, antinode_col2))

    print(len(antinodes))

if __name__ == '__main__':
    main()
