
def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.splitlines()

    len_row = len(lines)
    len_col = len(lines[0])

    start = (0, 1, "D")
    edges = []
    done = {}

    nodes = set()
    nodes.add((start[0], start[1]))
    temp_nodes = [start]
    while temp_nodes:
        current = temp_nodes.pop()
        current_row = current[0]
        current_col = current[1]
        current_move = current[2]
        done[(current_row, current_col)] = True
        nodes.add((current_row, current_col))

        neighbors = []

        if current_col > 0 and not lines[current_row][current_col - 1] in [">", "#"] and current_move != "R":
            left_neighbor = (current_row, current_col - 1, "L")
            neighbors.append(left_neighbor)
        if current_col < len_col - 1 and not lines[current_row][current_col + 1] in ["<", "#"] and current_move != "L":
            right_neighbor = (current_row, current_col + 1, "R")
            neighbors.append(right_neighbor)
        if current_row > 0 and not lines[current_row - 1][current_col] in ["v", "#"] and current_move != "D":
            up_neighbor = (current_row - 1, current_col, "U")
            neighbors.append(up_neighbor)
        if current_row < len_row - 1 and not lines[current_row + 1][current_col] in ["^", "#"] and current_move != "U":
            down_neighbor = (current_row + 1, current_col, "D")
            neighbors.append(down_neighbor)

        for neighbor in neighbors:
            neighbor_row = neighbor[0]
            neighbor_col = neighbor[1]
            edges.append(((current_row, current_col), (neighbor_row, neighbor_col)))
            if (neighbor_row, neighbor_col) not in done:
                temp_nodes.append(neighbor)

    dist = {}

    for node in nodes:
        dist[node] = 100000000

    dist[(0, 1)] = 0

    for _ in range(len(nodes) - 1):
        for edge in edges:
            u = edge[0]
            v = edge[1]
            if dist[u] - 1 < dist[v]:
                dist[v] = dist[u] - 1

    print(-dist[(len_row - 1, len_col - 2)])


if __name__ == '__main__':
    main()
