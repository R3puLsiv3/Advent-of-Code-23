
def down(tile, tiles, inner_tiles):
    current_tile = (tile[0], tile[1] + 1)
    while tiles[current_tile] is True:
        tiles[current_tile] = False
        inner_tiles += 1
        current_tile = (current_tile[0], current_tile[1] + 1)
    return inner_tiles


def up(tile, tiles, inner_tiles):
    current_tile = (tile[0], tile[1] - 1)
    while tiles[current_tile] is True:
        tiles[current_tile] = False
        inner_tiles += 1
        current_tile = (current_tile[0], current_tile[1] - 1)
    return inner_tiles


def left(tile, tiles, inner_tiles):
    current_tile = (tile[0] + 1, tile[1])
    while tiles[current_tile] is True:
        tiles[current_tile] = False
        inner_tiles += 1
        current_tile = (current_tile[0] + 1, current_tile[1])
    return inner_tiles


def right(tile, tiles, inner_tiles):
    current_tile = (tile[0] - 1, tile[1])
    while tiles[current_tile] is True:
        tiles[current_tile] = False
        inner_tiles += 1
        current_tile = (current_tile[0] - 1, current_tile[1])
    return inner_tiles


def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.splitlines()

    tiles = {}
    start = None
    for i, line in enumerate(lines):
        for j, tile in enumerate(line):
            tiles[(i, j)] = True
            if tile == "S":
                # Looking at my input tells me I need to go down (or up)
                start = [i, j, "DOWN"]

    current_tile = [start[0] + 1, start[1], None]
    prev_tile = start
    next_tile = None
    path = [start]
    # Save tiles of path with direction, so we can later look at the inner side of the path.
    while True:
        match lines[current_tile[0]][current_tile[1]]:
            case "|":
                if prev_tile[0] < current_tile[0]:
                    current_tile[2] = "DOWN"
                    next_tile = [current_tile[0] + 1, current_tile[1], None]
                else:
                    current_tile[2] = "UP"
                    next_tile = [current_tile[0] - 1, current_tile[1], None]
            case "-":
                if prev_tile[1] < current_tile[1]:
                    current_tile[2] = "RIGHT"
                    next_tile = [current_tile[0], current_tile[1] + 1, None]
                else:
                    current_tile[2] = "LEFT"
                    next_tile = [current_tile[0], current_tile[1] - 1, None]
            case "L":
                if prev_tile[0] < current_tile[0]:
                    current_tile[2] = "DOWN_RIGHT"
                    next_tile = [current_tile[0], current_tile[1] + 1, None]
                else:
                    current_tile[2] = "LEFT_UP"
                    next_tile = [current_tile[0] - 1, current_tile[1], None]
            case "J":
                if prev_tile[0] < current_tile[0]:
                    current_tile[2] = "DOWN_LEFT"
                    next_tile = [current_tile[0], current_tile[1] - 1, None]
                else:
                    current_tile[2] = "RIGHT_UP"
                    next_tile = [current_tile[0] - 1, current_tile[1], None]
            case "7":
                if prev_tile[0] > current_tile[0]:
                    current_tile[2] = "UP_LEFT"
                    next_tile = [current_tile[0], current_tile[1] - 1, None]
                else:
                    current_tile[2] = "RIGHT_DOWN"
                    next_tile = [current_tile[0] + 1, current_tile[1], None]
            case "F":
                if prev_tile[0] > current_tile[0]:
                    current_tile[2] = "UP_RIGHT"
                    next_tile = [current_tile[0], current_tile[1] + 1, None]
                else:
                    current_tile[2] = "LEFT_DOWN"
                    next_tile = [current_tile[0] + 1, current_tile[1], None]
            case "S":
                break
            case _:
                print("Unknown tile encountered")
                break

        path.append(current_tile)
        prev_tile = current_tile
        current_tile = next_tile

    for tile in path:
        tiles[(tile[0], tile[1])] = False

    # Look towards "inner" side of path for inner tiles. For different inputs left/right and up/down might need
    # to be reversed, since the algorithm doesn't know in advance which side is inner and which one outer.
    inner_tiles = 0
    for tile in path:
        match tile[2]:
            case "UP":
                inner_tiles = up(tile, tiles, inner_tiles)
            case "DOWN":
                inner_tiles = down(tile, tiles, inner_tiles)
            case "LEFT":
                inner_tiles = left(tile, tiles, inner_tiles)
            case "RIGHT":
                inner_tiles = right(tile, tiles, inner_tiles)
            case "DOWN_RIGHT":
                inner_tiles = down(tile, tiles, inner_tiles)
                inner_tiles = right(tile, tiles, inner_tiles)
            case "LEFT_UP":
                inner_tiles = left(tile, tiles, inner_tiles)
                inner_tiles = up(tile, tiles, inner_tiles)
            case "DOWN_LEFT":
                inner_tiles = down(tile, tiles, inner_tiles)
                inner_tiles = left(tile, tiles, inner_tiles)
            case "RIGHT_UP":
                inner_tiles = right(tile, tiles, inner_tiles)
                inner_tiles = up(tile, tiles, inner_tiles)
            case "UP_LEFT":
                inner_tiles = up(tile, tiles, inner_tiles)
                inner_tiles = left(tile, tiles, inner_tiles)
            case "RIGHT_DOWN":
                inner_tiles = right(tile, tiles, inner_tiles)
                inner_tiles = down(tile, tiles, inner_tiles)
            case "UP_RIGHT":
                inner_tiles = up(tile, tiles, inner_tiles)
                inner_tiles = right(tile, tiles, inner_tiles)
            case "LEFT_DOWN":
                inner_tiles = left(tile, tiles, inner_tiles)
                inner_tiles = down(tile, tiles, inner_tiles)
            case _:
                continue

    print(inner_tiles)


if __name__ == '__main__':
    main()
