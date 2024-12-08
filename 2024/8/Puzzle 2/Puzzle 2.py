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
            dist_vertical = row1 - row2
            dist_horizontal = col1 - col2

            antinodes.add((row1, col1))

            antinode_row = row1 + dist_vertical
            antinode_col = col1 + dist_horizontal

            while True:
                if 0 <= antinode_row < height and 0 <= antinode_col < length:
                    antinodes.add((antinode_row, antinode_col))
                    antinode_row += dist_vertical
                    antinode_col += dist_horizontal
                else:
                    break

            antinode_row = row1 - dist_vertical
            antinode_col = col1 - dist_horizontal

            while True:
                if 0 <= antinode_row < height and 0 <= antinode_col < length:
                    antinodes.add((antinode_row, antinode_col))
                    antinode_row -= dist_vertical
                    antinode_col -= dist_horizontal
                else:
                    break

    print(len(antinodes))

if __name__ == '__main__':
    main()
