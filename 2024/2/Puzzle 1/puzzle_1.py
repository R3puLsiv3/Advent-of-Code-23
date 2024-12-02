
def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.split("\n")
    levels_list = list(map(lambda x: list(map(int, x.split(" "))), lines))

    result = 0
    for levels in levels_list:
        if (all(levels[i] > levels[i + 1] and abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))
            or all(levels[i] < levels[i + 1] and abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))):
            result += 1

    print(result)

if __name__ == '__main__':
    main()
