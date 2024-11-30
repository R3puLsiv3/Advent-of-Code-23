
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
        max_cubes = {"red": 0, "green": 0, "blue": 0}
        for draw in game:
            if draw["red"] > max_cubes["red"]:
                max_cubes["red"] = draw["red"]
            if draw["green"] > max_cubes["green"]:
                max_cubes["green"] = draw["green"]
            if draw["blue"] > max_cubes["blue"]:
                max_cubes["blue"] = draw["blue"]
        result += max_cubes["red"] * max_cubes["green"] * max_cubes["blue"]

    print(result)


if __name__ == '__main__':
    main()
