
def main():
    with open("input.txt") as f:
        data = f.read()
    data = data.replace(" ", "")
    lines = data.splitlines()

    parsed_data = []
    for i, line in enumerate(lines):
        colon_split = line.split(":")
        semi_colon_split = colon_split[1].split(";")

        parsed_data.append([])
        for j, subset in enumerate(semi_colon_split):
            subset = subset.split(",")

            colors = {"red": 0, "green": 0, "blue": 0}
            parsed_data[i].append(colors)
            for cubes in subset:
                if cubes.endswith("red"):
                    parsed_data[i][j]["red"] = (int(cubes.removesuffix("red")))
                elif cubes.endswith("green"):
                    parsed_data[i][j]["green"] = (int(cubes.removesuffix("green")))
                else:
                    parsed_data[i][j]["blue"] = (int(cubes.removesuffix("blue")))

    result = 0
    for index, game in enumerate(parsed_data):
        legal_game = True
        for draw in game:
            if draw["red"] > 12 or draw["green"] > 13 or draw["blue"] > 14:
                legal_game = False
        if legal_game:
            result += index + 1

    print(result)


if __name__ == '__main__':
    main()
