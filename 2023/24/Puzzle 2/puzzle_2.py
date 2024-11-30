import sympy as sy


class Hailstone:
    def __init__(self, x_pos, y_pos, z_pos, x_delta, y_delta, z_delta):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.z_pos = z_pos
        self.x_delta = x_delta
        self.y_delta = y_delta
        self.z_delta = z_delta


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

    x, y, z, a, b, c = sy.symbols("x, y, z, a, b, c", int=True)
    sym = sy.symbols("s, t, u", int=True)

    terms = []
    for i, hailstone in enumerate(hailstones[:3]):
        t = sym[i]
        terms += [x + t*a - hailstone.x_pos - t*hailstone.x_delta, y + t*b - hailstone.y_pos - t*hailstone.y_delta,
                  z + t*c - hailstone.z_pos - t*hailstone.z_delta]

    result = list(sy.nonlinsolve(terms, [x, y, z, a, b, c, sym[0], sym[1], sym[2]]))

    print(result[0][0] + result[0][1] + result[0][2])


if __name__ == '__main__':
    main()
