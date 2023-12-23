import queue


def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.split()

    len_row = len(lines)
    len_col = len(lines[0])

    dist = {}
    done = {}
    seen = {}
    prio_queue = queue.PriorityQueue()

    dist[(0, 0, "")] = 0
    seen[(0, 0, "")] = True
    done[(0, 0, "")] = True
    dist[(0, 1, "")] = int(lines[0][1])
    seen[(0, 1, "")] = True
    dist[(1, 0, "")] = int(lines[1][0])
    seen[(1, 0, "")] = True
    prio_queue.put((int(lines[0][1]), (0, 1, "")))
    prio_queue.put((int(lines[1][0]), (1, 0, "")))

    while not prio_queue.empty():
        current = prio_queue.get()
        current_row = current[1][0]
        current_col = current[1][1]
        current_move = current[1][2]

        neighbors = []
        if current_col > 0 and current_move != "LLL":
            if current_move == "LL":
                next_move = "LLL"
            elif current_move == "L":
                next_move = "LL"
            else:
                next_move = "L"
            left_neighbor = (current_row, current_col - 1, next_move)
            neighbors.append(left_neighbor)
        if current_col < len_col - 1 and current_move != "RRR":
            if current_move == "RR":
                next_move = "RRR"
            elif current_move == "R":
                next_move = "RR"
            else:
                next_move = "R"
            right_neighbor = (current_row, current_col + 1, next_move)
            neighbors.append(right_neighbor)

        if current_row > 0 and current_move != "UUU":
            if current_move == "UU":
                next_move = "UUU"
            elif current_move == "U":
                next_move = "UU"
            else:
                next_move = "U"
            up_neighbor = (current_row - 1, current_col, next_move)
            neighbors.append(up_neighbor)

        if current_row < len_row - 1 and current_move != "DDD":
            if current_move == "DD":
                next_move = "DDD"
            elif current_move == "D":
                next_move = "DD"
            else:
                next_move = "D"
            down_neighbor = (current_row + 1, current_col, next_move)
            neighbors.append(down_neighbor)

        for neighbor in neighbors:
            if neighbor in done:
                continue
            if neighbor not in done:
                new_dist = dist[current[1]] + int(lines[neighbor[0]][neighbor[1]])
                if neighbor not in dist:
                    dist[neighbor] = new_dist
                    if neighbor not in seen:
                        prio_queue.put((new_dist, neighbor))
                        seen[neighbor] = True
                elif new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    if neighbor not in seen:
                        prio_queue.put((new_dist, neighbor))
                        seen[neighbor] = True
            done[current] = True

    result = []
    if (len_row - 1, len_col - 1, "R") in dist:
        result.append(dist[(len_row - 1, len_col - 1, "R")])
    if (len_row - 1, len_col - 1, "RR") in dist:
        result.append(dist[(len_row - 1, len_col - 1, "RR")])
    if (len_row - 1, len_col - 1, "RRR") in dist:
        result.append(dist[(len_row - 1, len_col - 1, "RRR")])
    if (len_row - 1, len_col - 1, "D") in dist:
        result.append(dist[(len_row - 1, len_col - 1, "D")])
    if (len_row - 1, len_col - 1, "DD") in dist:
        result.append(dist[(len_row - 1, len_col - 1, "DD")])
    if (len_row - 1, len_col - 1, "DDD") in dist:
        result.append(dist[(len_row - 1, len_col - 1, "DDD")])

    print(min(result))


if __name__ == '__main__':
    main()
