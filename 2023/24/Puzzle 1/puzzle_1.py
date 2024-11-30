import numpy as np


class Hailstone:
    def __init__(self, x_pos, y_pos, z_pos, x_delta, y_delta, z_delta):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.z_pos = z_pos
        self.x_delta = x_delta
        self.y_delta = y_delta
        self.z_delta = z_delta

        self.x_dir = np.sign(x_delta)

        self.m = (y_pos + y_delta - y_pos) / (x_pos + x_delta - x_pos)
        self.b = y_pos - self.m * x_pos

        self.func = lambda x: self.m*x + self.b


def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.splitlines()
    data = data.replace(" ", "")

    hailstones = []

    for line in lines:
        at_split = line.split("@")
        pos = [int(x) for x in at_split[0].split(",")]
        delta = [int(x) for x in at_split[1].split(",")]
        hailstone = Hailstone(*(pos + delta))
        hailstones.append(hailstone)

    result = 0
    for hailstone_1 in hailstones:
        for hailstone_2 in hailstones:
            if hailstone_1 is hailstone_2:
                continue
            elif hailstone_1.m == hailstone_2.m and hailstone_1.b == hailstone_2.b:
                result += 1
                continue
            elif hailstone_1.m == hailstone_2.m:
                continue
            else:
                x_intersect = (hailstone_2.b - hailstone_1.b) / (hailstone_1.m - hailstone_2.m)
                y_intersect = hailstone_1.func(x_intersect)

                if hailstone_1.x_dir * x_intersect < hailstone_1.x_dir * hailstone_1.x_pos:
                    continue
                if hailstone_2.x_dir * x_intersect < hailstone_2.x_dir * hailstone_2.x_pos:
                    continue

                if 200000000000000 <= x_intersect <= 400000000000000\
                        and 200000000000000 <= y_intersect <= 400000000000000:
                    result += 1

    print(result // 2)


if __name__ == '__main__':
    main()
