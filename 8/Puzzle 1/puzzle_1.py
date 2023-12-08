
def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.splitlines()
    instructions = [int(x) for x in list(lines[0].replace("L", "0").replace("R", "1"))]

    nodes = {}
    for line in lines[2:]:
        equal_split = line.split(" = ")
        start_point = equal_split[0]
        end_point = (equal_split[1][1:4], equal_split[1][6:9])
        nodes[start_point] = end_point

    current_node = "AAA"
    count = 0
    while True:
        count += 1
        for direction in instructions:
            current_node = nodes[current_node][direction]
        if current_node == "ZZZ":
            break

    print(count * len(instructions))


if __name__ == '__main__':
    main()
