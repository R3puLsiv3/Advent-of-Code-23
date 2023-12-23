
def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.splitlines()

    directions = []
    lengths = []
    dir_dict = {"0": "R", "1": "D", "2": "L", "3": "U"}
    for line in lines:
        new_instructions = line.split()[2]
        directions.append(dir_dict[new_instructions[-2]])
        lengths.append(int(new_instructions[2:7], 16))

    x = 0
    y = 0
    current_position = (x, y)
    positions = [current_position]
    for i, direction in enumerate(directions):
        match direction:
            case "L":
                x -= lengths[i]
                positions.append((x, y))
            case "R":
                x += lengths[i]
                positions.append((x, y))
            case "U":
                y += lengths[i]
                positions.append((x, y))
            case "D":
                y -= lengths[i]
                positions.append((x, y))

    area = 0
    for i in range(len(positions) - 1):
        area += (positions[i][1] + positions[i+1][1]) * (positions[i][0] - positions[i+1][0]) - lengths[i]

    area //= 2
    print(abs(area) + 1)


if __name__ == '__main__':
    main()
