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

    dist[(0, 0, "", 0)] = 0
    seen[(0, 0, "", 0)] = True
    done[(0, 0, "", 0)] = True
    dist[(0, 1, "R", 1)] = int(lines[0][1])
    seen[(0, 1, "R", 1)] = True
    dist[(1, 0, "D", 1)] = int(lines[1][0])
    seen[(1, 0, "D", 1)] = True
    prio_queue.put((int(lines[0][1]), (0, 1, "R", 1)))
    prio_queue.put((int(lines[1][0]), (1, 0, "D", 1)))

    while not prio_queue.empty():
        current = prio_queue.get()
        current_row = current[1][0]
        current_col = current[1][1]
        current_move = current[1][2]
        current_num = current[1][3]

        neighbors = []

        if current_num < 4:
            match current_move:
                case "L":
                    neighbors.append((current_row, current_col - 1, "L", current_num + 1))
                case "R":
                    neighbors.append((current_row, current_col + 1, "R", current_num + 1))
                case "U":
                    neighbors.append((current_row - 1, current_col, "U", current_num + 1))
                case "D":
                    neighbors.append((current_row + 1, current_col, "D", current_num + 1))
        elif current_num == 10:
            if current_move != "L" and current_col > 3 and current_move != "R":
                neighbors.append((current_row, current_col - 1, "L", 1))
            if current_move != "R" and current_col < len_col - 4 and current_move != "L":
                neighbors.append((current_row, current_col + 1, "R", 1))
            if current_move != "U" and current_row > 3 and current_move != "D":
                neighbors.append((current_row - 1, current_col, "U", 1))
            if current_move != "D" and current_row < len_row - 4 and current_move != "U":
                neighbors.append((current_row + 1, current_col, "D", 1))
        else:
            if current_col > 0:
                if current_move == "L":
                    neighbors.append((current_row, current_col - 1, "L", current_num + 1))
                elif current_col > 3 and current_move != "R":
                    neighbors.append((current_row, current_col - 1, "L", 1))
            if current_col < len_col - 1:
                if current_move == "R":
                    neighbors.append((current_row, current_col + 1, "R", current_num + 1))
                elif current_col < len_col - 4 and current_move != "L":
                    neighbors.append((current_row, current_col + 1, "R", 1))
            if current_row > 0:
                if current_move == "U":
                    neighbors.append((current_row - 1, current_col, "U", current_num + 1))
                elif current_row > 3 and current_move != "D":
                    neighbors.append((current_row - 1, current_col, "U", 1))
            if current_row < len_row - 1:
                if current_move == "D":
                    neighbors.append((current_row + 1, current_col, "D", current_num + 1))
                elif current_row < len_row - 4 and current_move != "U":
                    neighbors.append((current_row + 1, current_col, "D", 1))

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
    for i in range(4, 11):
        if (len_row - 1, len_col - 1, "R", i) in dist:
            result.append(dist[(len_row - 1, len_col - 1, "R", i)])
    for i in range(4, 11):
        if (len_row - 1, len_col - 1, "D", i) in dist:
            result.append(dist[(len_row - 1, len_col - 1, "D", i)])

    print(min(result))


if __name__ == '__main__':
    main()
