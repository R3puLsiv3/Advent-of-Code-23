
def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.splitlines()

    start = None
    for i, line in enumerate(lines):
        for j, tile in enumerate(line):
            if tile == "S":
                start = (i, j)

    # Looking at my input tells me I need to go up (or down)
    current_tile = (start[0] - 1, start[1])
    prev_tile = start
    next_tile = None
    path = [start]
    while True:
        match lines[current_tile[0]][current_tile[1]]:
            case "|":
                if prev_tile[0] < current_tile[0]:
                    next_tile = (current_tile[0] + 1, current_tile[1])
                else:
                    next_tile = (current_tile[0] - 1, current_tile[1])
            case "-":
                if prev_tile[1] < current_tile[1]:
                    next_tile = (current_tile[0], current_tile[1] + 1)
                else:
                    next_tile = (current_tile[0], current_tile[1] - 1)
            case "L":
                if prev_tile[0] < current_tile[0]:
                    next_tile = (current_tile[0], current_tile[1] + 1)
                else:
                    next_tile = (current_tile[0] - 1, current_tile[1])
            case "J":
                if prev_tile[0] < current_tile[0]:
                    next_tile = (current_tile[0], current_tile[1] - 1)
                else:
                    next_tile = (current_tile[0] - 1, current_tile[1])
            case "7":
                if prev_tile[0] > current_tile[0]:
                    next_tile = (current_tile[0], current_tile[1] - 1)
                else:
                    next_tile = (current_tile[0] + 1, current_tile[1])
            case "F":
                if prev_tile[0] > current_tile[0]:
                    next_tile = (current_tile[0], current_tile[1] + 1)
                else:
                    next_tile = (current_tile[0] + 1, current_tile[1])
            case "S":
                break
            case _:
                print("Unknown tile encountered")
                break

        path.append(current_tile)
        prev_tile = current_tile
        current_tile = next_tile

    print(len(path) // 2)


if __name__ == '__main__':
    main()
