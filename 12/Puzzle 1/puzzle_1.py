
def find_arrangements(blocks, values):
    if not (blocks or values) or (all(char == "?" for block in blocks for char in block) and not values):
        return 1
    elif (blocks and not values) or (not blocks and values):
        return 0
    else:
        block = blocks.pop()
        value = values.pop()

        if len(block) < value:
            if "#" in block:
                return 0
            else:
                return find_arrangements(list(blocks), list(values) + [value])

        result = 0
        if "#" not in block:
            result += find_arrangements(list(blocks), list(values) + [value])

        possibilities = len(block) - value + 1
        for i in range(possibilities):
            block_left = block[:i]
            block_right = block[i + value:]

            if "#" in block_left:
                break
            elif block_right.startswith("#"):
                continue
            elif not block_right:
                result += find_arrangements(list(blocks), list(values))
            else:
                result += find_arrangements(list(blocks) + [block_right[1:]], list(values))
        return result


def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.splitlines()
    rows = []
    values = []
    for line in lines:
        line = line.split()
        rows.append(line[0] + ".")
        value = [int(x) for x in line[1].split(",")]
        value.reverse()
        values.append(value)

    blocks = []
    for row in rows:
        block = ""
        blocks_per_line = []
        for char in row:
            match char:
                case "?":
                    block += char
                case ".":
                    if block:
                        blocks_per_line.append(block)
                        block = ""
                case "#":
                    block += char
        blocks_per_line.reverse()
        blocks.append(blocks_per_line)

    result = 0

    for i in range(len(blocks)):
        result += find_arrangements(blocks[i], values[i])

    print(result)


if __name__ == '__main__':
    main()
