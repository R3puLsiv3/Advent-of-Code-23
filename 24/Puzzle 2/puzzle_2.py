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
    # This was solved by using an external LGS solver. The sympy LGS solver somehow doesn't consider necessary
    # boundaries for variables and only tries to find a general solution, which fails.
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

    sym = sy.symbols("t_0 t_1 t_2", real=True)
    matrix = sy.Matrix()
    b = sy.Matrix()
    for i, hailstone in enumerate(hailstones[:3]):
        t = sym[i]
        to_append = sy.Matrix([[1, 0, 0, t, 0, 0],
                              [0, 1, 0, 0, t, 0],
                              [0, 0, 1, 0, 0, t]])
        matrix = matrix.row_insert(0, to_append)

        to_append = sy.Matrix([[hailstone.x_pos + t*hailstone.x_delta],
                              [hailstone.y_pos + t*hailstone.y_delta],
                              [hailstone.z_pos + t*hailstone.z_delta]])

        b = b.row_insert(0, to_append)

    result = list(sy.linsolve((matrix, b)))

    print(result)


if __name__ == '__main__':
    main()
