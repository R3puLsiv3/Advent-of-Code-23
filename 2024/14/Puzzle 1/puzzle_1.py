import numpy as np
import re

def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.split("\n")

    positions = []
    velocities = []
    for line in lines:
        match = re.search("p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
        positions.append((np.array([match.group(1), match.group(2)], dtype=int)))
        velocities.append((np.array([match.group(3), match.group(4)], dtype=int)))

    new_positions = []
    for position, velocity in zip(positions, velocities):
        change_after_100 = 5 * velocity
        position = position + change_after_100
        position = np.mod(position, np.array([101, 103]))
        new_positions.append(position)

    split_horizontal = 101 // 2
    split_vertical = 103 // 2
    left_top = [position for position in new_positions if position[0] < split_horizontal and position[1] < split_vertical]
    left_bottom = [position for position in new_positions if position[0] < split_horizontal and position[1] > split_vertical]
    right_top = [position for position in new_positions if position[0] > split_horizontal and position[1] < split_vertical]
    right_bottom = [position for position in new_positions if position[0] > split_horizontal and position[1] > split_vertical]

    print(len(left_top), len(right_top))
    print(len(left_bottom), len(right_bottom))
    print(len(left_top) * len(left_bottom) * len(right_top) * len(right_bottom))

if __name__ == '__main__':
    main()
