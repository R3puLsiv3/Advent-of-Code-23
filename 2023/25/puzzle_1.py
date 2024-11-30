import copy
import random


def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.splitlines()

    edges = {}
    for line in lines:
        colon_split = line.split(": ")
        left_edge = colon_split[0]
        right_edges = colon_split[1].split(" ")

        if left_edge not in edges:
            edges[left_edge] = []

        for r_e in right_edges:
            edges[left_edge].append(r_e)

            if r_e not in edges:
                edges[r_e] = []

            edges[r_e].append(left_edge)

    while True:
        new_edges = copy.deepcopy(edges)
        while len(new_edges) > 2:
            vertex = random.choice(list(new_edges.keys()))
            second_vertex = random.choice(new_edges[vertex])

            new_edges[vertex] = [x for x in new_edges[vertex] if x != second_vertex]
            new_edges[second_vertex] = [x for x in new_edges[second_vertex] if x != vertex]

            new_vertex = vertex + second_vertex
            new_edges[new_vertex] = new_edges[vertex] + new_edges[second_vertex]
            del new_edges[vertex]
            del new_edges[second_vertex]

            for third_vertex in new_edges[new_vertex]:
                for v in new_edges[third_vertex]:
                    if v == vertex or v == second_vertex:
                        new_edges[third_vertex].remove(v)
                        new_edges[third_vertex].append(new_vertex)

        first = list(new_edges.keys())[0]
        if len(new_edges[first]) == 3:
            break

    second = list(new_edges.keys())[1]
    print((len(first) // 3) * (len(second) // 3))






if __name__ == '__main__':
    main()
