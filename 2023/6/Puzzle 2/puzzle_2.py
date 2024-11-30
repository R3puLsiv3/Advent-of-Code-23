import math


def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.splitlines()
    total_time = int(lines[0].split(":")[1].replace(" ", ""))
    distance = int(lines[1].split(":")[1].replace(" ", ""))

    # Solve quadratic equation (time - x)*x = distance <=> -x^2 + time*x - distance = 0
    discriminant_sqrt = math.sqrt(total_time ** 2 - 4 * distance)
    root1 = (total_time - discriminant_sqrt) // 2
    root2 = (total_time + discriminant_sqrt) // 2
    result = int(abs(root1-root2))

    print(result)


if __name__ == '__main__':
    main()
