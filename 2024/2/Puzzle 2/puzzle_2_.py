def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.split("\n")
    levels_list = list(map(lambda x: list(map(int, x.split(" "))), lines))

    # Joke solution in one line
    # print(sum([1 for checks in
    #            [[True for dampened_levels in [[*levels[0:i], *levels[i + 1:]] for i in range(len(levels))] if
    #              all(dampened_levels[i] > dampened_levels[i + 1] and abs(
    #                  dampened_levels[i] - dampened_levels[i + 1]) <= 3 for i in
    #                   range(len(dampened_levels) - 1))
    #               or all(
    #                          dampened_levels[i] < dampened_levels[i + 1] and abs(
    #                              dampened_levels[i] - dampened_levels[i + 1]) <= 3 for i in
    #                          range(len(dampened_levels) - 1))] for levels in
    #             list(map(lambda x: list(map(int, x.split(" "))), data.split("\n")))] if len(checks) > 0]))

    result = 0
    for levels in levels_list:
        if (all(levels[i] > levels[i + 1] and abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))
                or all(
                    levels[i] < levels[i + 1] and abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))):
            result += 1
        else:
            for i in range(len(levels)):
                dampened_levels = list(levels)
                del dampened_levels[i]
                if (all(dampened_levels[i] > dampened_levels[i + 1] and abs(
                        dampened_levels[i] - dampened_levels[i + 1]) <= 3 for i in
                        range(len(dampened_levels) - 1))
                        or all(
                            dampened_levels[i] < dampened_levels[i + 1] and abs(
                                dampened_levels[i] - dampened_levels[i + 1]) <= 3 for i in
                            range(len(dampened_levels) - 1))):
                    result += 1
                    break

    print(result)


if __name__ == '__main__':
    main()
