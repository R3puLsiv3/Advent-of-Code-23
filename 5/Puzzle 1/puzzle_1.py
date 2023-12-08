
def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.splitlines()
    seeds_split = lines[0].split(":")
    seeds = [int(x) for x in seeds_split[1].strip().split()]

    mappings = {}
    current_mapping = ""
    for line in lines[2:]:
        if not line:
            continue
        elif line[0].isalpha():
            current_mapping = line.split(":")[0]
            mappings[current_mapping] = {}
        elif line[0].isdigit():
            split_numbers = line.split()
            dst = int(split_numbers[0])
            src = int(split_numbers[1])
            rng = int(split_numbers[2])
            mappings[current_mapping][(src, rng)] = dst

    result = []
    for seed in seeds:
        for mapping in mappings:
            for map_ in mappings[mapping]:
                lower = map_[0]
                range_ = map_[1] - 1
                upper = lower + range_
                if lower <= seed <= upper:
                    seed = mappings[mapping][map_] + seed - lower
                    break
        result.append(seed)

    print(min(result))


if __name__ == '__main__':
    main()
