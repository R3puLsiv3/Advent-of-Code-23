import operator


def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.split("\n")
    l1 = []
    l2 = []
    for line in lines:
        values = line.split("   ")
        left = int(values[0])
        l1.append(left)
        right = int(values[1])
        l2.append(right)

    l1.sort()
    l2.sort()

    result = sum([abs(x - y) for (x, y) in zip(l1, l2)])
    print(result)

if __name__ == '__main__':
    main()
