import numpy as np
import re
import sys


def main():
    np.set_printoptions(threshold=sys.maxsize)
    with open("input.txt") as f:
        data = f.read()

    lines = data.split("\n")

    positions = []
    velocities = []
    for line in lines:
        match = re.search("p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
        positions.append((np.array([match.group(1), match.group(2)], dtype=int)))
        velocities.append((np.array([match.group(3), match.group(4)], dtype=int)))

    seconds = 0
    while True:
        new_positions = []
        seconds += 1
        for position, velocity in zip(positions, velocities):
            position = position + seconds * velocity
            position = np.mod(position, np.array([101, 103]))
            new_positions.append(position)

        # I checked beforehand if the variation reaches a low point at some second. The variance threshold might need
        # to be adjusted for different inputs.
        var = np.var(new_positions)
        if var < 500:
            break

    print(seconds)

if __name__ == '__main__':
    main()
