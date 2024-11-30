
def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.splitlines()
    times = [int(x) for x in lines[0].split(":")[1].split()]
    distances = [int(x) for x in lines[1].split(":")[1].split()]

    number_of_ways = {0: 0, 1: 0, 2: 0, 3: 0}
    for race in range(4):
        for hold_time in range(times[race] + 1):
            race_time = times[race] - hold_time
            race_distance = race_time * hold_time
            if race_distance > distances[race]:
                number_of_ways[race] += 1

    result = 1
    for race in number_of_ways:
        result *= number_of_ways[race]

    print(result)


if __name__ == '__main__':
    main()
