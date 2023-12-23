import copy
import queue
import sys


class Block:
    def __init__(self, name, x_start, y_start, z_start, x_end, y_end, z_end):
        self.name = name
        self.x_start = x_start
        self.y_start = y_start
        self.z_start = z_start
        self.x_end = x_end
        self.y_end = y_end
        self.z_end = z_end
        self.above = set()
        self.below = set()

    def __str__(self):
        return f"({self.x_start}, {self.y_start}, {self.z_start}) - ({self.x_end}, {self.y_end}, {self.z_end})"

    def __repr__(self):
        return str(self.name)


def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.splitlines()

    sys.setrecursionlimit(10000)

    blocks = []
    for i, line in enumerate(lines):
        tilde_split = line.split("~")
        start_ranges = tilde_split[0].split(",")
        end_ranges = tilde_split[1].split(",")
        blocks.append(Block(*([i] + [int(x) for x in start_ranges] + [int(x) for x in end_ranges])))

    blocks.sort(key=lambda b: b.z_start)

    occupied = {}

    for block in blocks:
        z = block.z_start
        found = False
        while z != 0 and not found:
            for x in range(block.x_start, block.x_end + 1):
                for y in range(block.y_start, block.y_end + 1):
                    if (x, y, z) in occupied:
                        found = True
                        occupied[(x, y, z)].above.add(block)
                        block.below.add(occupied[(x, y, z)])
            if not found:
                z -= 1

        if found:
            z += 1 + block.z_end - block.z_start
        else:
            z = 1 + block.z_end - block.z_start

        for x in range(block.x_start, block.x_end + 1):
            for y in range(block.y_start, block.y_end + 1):
                occupied[(x, y, z)] = block

    result = 0
    for i in range(len(blocks)):
        print(i)
        # The entire blocks structure needs to be reset, deepcopy is extremely slow. In an actual application you should
        # use json dumps or cPickle or mark the nodes.
        new_blocks = copy.deepcopy(blocks)
        block = new_blocks[i]
        parents_queue = queue.Queue()
        parents_queue.put((block, block.above))
        while not parents_queue.empty():
            current_parents = parents_queue.get()
            current_block = current_parents[0]
            parents = current_parents[1]
            if not parents:
                continue

            for parent in parents:
                below = parent.below
                if current_block in below:
                    below.remove(current_block)
                if not below:
                    result += 1
                    parents_queue.put((parent, parent.above))
                    continue

    print(result)


if __name__ == '__main__':
    main()
