import math


def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.splitlines()
    instructions = [int(x) for x in list(lines[0].replace("L", "0").replace("R", "1"))]

    nodes = {}
    start_points = []
    end_points = []
    for line in lines[2:]:
        equal_split = line.split(" = ")
        start_point = equal_split[0]
        if start_point[2] == "A":
            start_points.append(start_point)
        elif start_point[2] == "Z":
            end_points.append(start_point)
        end_point = (equal_split[1][1:4], equal_split[1][6:9])
        nodes[start_point] = end_point

    steps_per_node = {}
    for node in start_points:
        current_node = node
        count = 0
        while True:
            count += 1
            for direction in instructions:
                current_node = nodes[current_node][direction]
            if current_node in end_points:
                break

        steps_per_node[node] = count * len(instructions)

    print(math.lcm(*steps_per_node.values()))


if __name__ == '__main__':
    main()
