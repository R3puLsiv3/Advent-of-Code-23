def move_guard(lines, pos_guard, direction):
    match direction:
        case "<":
            if lines[pos_guard[0]][pos_guard[1] - 1] == "#":
                direction = turn_guard(direction)
            else:
                pos_guard = (pos_guard[0], pos_guard[1] - 1)
        case ">":
            if lines[pos_guard[0]][pos_guard[1] + 1] == "#":
                direction = turn_guard(direction)
            else:
                pos_guard = (pos_guard[0], pos_guard[1] + 1)
        case "^":
            if lines[pos_guard[0] - 1][pos_guard[1]] == "#":
                direction = turn_guard(direction)
            else:
                pos_guard = (pos_guard[0] - 1, pos_guard[1])
        case "v":
            if lines[pos_guard[0] + 1][pos_guard[1]] == "#":
                direction = turn_guard(direction)
            else:
                pos_guard = (pos_guard[0] + 1, pos_guard[1])
    return pos_guard, direction

def turn_guard(direction):
    match direction:
        case "<":
            return "^"
        case ">":
            return "v"
        case "^":
            return ">"
        case "v":
            return "<"

def build_obstacle(lines, tile_pos):
    original_tile = lines[tile_pos[0]][tile_pos[1]]
    lines[tile_pos[0]] = lines[tile_pos[0]][:tile_pos[1]] + "#" + lines[tile_pos[0]][tile_pos[1] + 1:]
    return original_tile

def clear_obstacle(lines, tile_pos, tile):
    lines[tile_pos[0]] = lines[tile_pos[0]][:tile_pos[1]] + tile + lines[tile_pos[0]][tile_pos[1] + 1:]

def check_obstacle(lines, pos_guard, direction):
    visited = {(pos_guard, direction): True}
    while lines[pos_guard[0]][pos_guard[1]] not in ["X"]:
        visited[(pos_guard, direction)] = True
        pos_guard, direction = move_guard(lines, pos_guard, direction)
        if (pos_guard, direction) in visited:
            return True
    return False

def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.split("\n")
    length = len(lines[0])
    padding = 1
    # Add padding so it's not necessary to check for boundaries later.
    lines = ["X" * (length + 2 * padding)] * padding + ["X" * padding + line + "X" * padding for line in lines] + [
        "X" * (length + 2 * padding)] * padding

    original_pos_guard, original_direction = [((row_idx, col_idx), tile) for row_idx, row in enumerate(lines) for col_idx, tile in enumerate(row) if tile in ["<", ">", "^", "v"]].pop()
    path = set()
    pos_guard = original_pos_guard
    direction = original_direction
    while lines[pos_guard[0]][pos_guard[1]] != "X":
        if lines[pos_guard[0]][pos_guard[1]] not in ["<", ">", "^", "v"]:
            path.add(pos_guard)
        pos_guard, direction = move_guard(lines, pos_guard, direction)

    # Very brute force implementation that places an obstacle at every tile on the path of the guard and then
    # checks if a cycle occurs when the guard is simulated. A faster method would be to create a graph of all obstacles
    # and thereby ignore all the steps inbetween.
    possible_obstacles = 0
    for tile_pos in path:
        original_tile = build_obstacle(lines, tile_pos)
        if  check_obstacle(lines, original_pos_guard, original_direction):
            possible_obstacles += 1
        clear_obstacle(lines, tile_pos, original_tile)

    print(possible_obstacles)

if __name__ == '__main__':
    main()