import sys


def find_lengths(current_node, current_len, edges_dict, lengths):
    if current_node == (140, 139):
        lengths.append(current_len)

    if current_node not in edges_dict:
        return
    children = edges_dict[current_node]

    new_dict = dict(edges_dict)
    del new_dict[current_node]

    for child in children:
        find_lengths(child[0], current_len + child[1], new_dict, lengths)


def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.splitlines()

    sys.setrecursionlimit(10000)

    len_row = len(lines)
    len_col = len(lines[0])

    start = (1, 1, "D")
    edges = set()
    done = {}

    nodes = set()
    nodes.add((0, 1))
    temp_nodes = [(start, (0, 1, "D"), 1)]
    while temp_nodes:
        current = temp_nodes.pop()
        current_row = current[0][0]
        current_col = current[0][1]
        current_move = current[0][2]
        parent = current[1]
        current_weight = current[2]
        done[(current_row, current_col)] = True

        neighbors = []

        if (current_row, current_col) == (len_row - 1, len_col - 2):
            edges.add(((parent[0], parent[1]), (current_row, current_col), current_weight))
            edges.add(((current_row, current_col), (parent[0], parent[1]), current_weight))
            nodes.add((current_row, current_col))
            continue

        if current_col > 0 and not lines[current_row][current_col - 1] in ["#"] and current_move != "R":
            left_neighbor = (current_row, current_col - 1, "L")
            neighbors.append(left_neighbor)
        if current_col < len_col - 1 and not lines[current_row][current_col + 1] in ["#"] and current_move != "L":
            right_neighbor = (current_row, current_col + 1, "R")
            neighbors.append(right_neighbor)
        if current_row > 0 and not lines[current_row - 1][current_col] in ["#"] and current_move != "D":
            up_neighbor = (current_row - 1, current_col, "U")
            neighbors.append(up_neighbor)
        if current_row < len_row - 1 and not lines[current_row + 1][current_col] in ["#"] and current_move != "U":
            down_neighbor = (current_row + 1, current_col, "D")
            neighbors.append(down_neighbor)

        if len(neighbors) > 1:
            edges.add(((parent[0], parent[1]), (current_row, current_col), current_weight))
            edges.add(((current_row, current_col), (parent[0], parent[1]), current_weight))
            nodes.add((current_row, current_col))

            for neighbor in neighbors:
                if (neighbor[0], neighbor[1]) not in done:
                    temp_nodes.append((neighbor, current[0], 1))

        if len(neighbors) <= 1:
            for neighbor in neighbors:
                temp_nodes.append((neighbor, parent, current_weight + 1))

    edges_dict = {}
    for edge in edges:
        if edge[0] not in edges_dict:
            edges_dict[edge[0]] = [(edge[1], edge[2])]
        else:
            edges_dict[edge[0]].append((edge[1], edge[2]))

    lengths = []
    find_lengths((0, 1), 0, edges_dict, lengths)

    print(max(lengths))


if __name__ == '__main__':
    main()
