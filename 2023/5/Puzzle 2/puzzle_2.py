
def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.splitlines()
    seeds_split = lines[0].split(":")
    seeds = [int(x) for x in seeds_split[1].strip().split()]
    seeds_ranges = set(zip(seeds[::2], seeds[1::2]))

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

    for mapping in mappings:
        total_ranges = set()
        while seeds_ranges:
            seed_range = seeds_ranges.pop()
            hit = False
            for map_ in mappings[mapping]:
                map_lower = map_[0]
                map_upper = map_[0] + map_[1] - 1
                seed_lower = seed_range[0]
                seed_upper = seed_range[0] + seed_range[1] - 1
                if map_lower <= seed_lower <= seed_upper <= map_upper:
                    dst_lower = mappings[mapping][map_]
                    offset_lower = seed_lower - map_lower
                    rng = seed_range[1]
                    total_ranges.add((dst_lower + offset_lower, rng))
                    hit = True
                elif seed_lower < map_lower <= seed_upper <= map_upper:
                    rng1 = map_lower - seed_lower
                    seeds_ranges.add((seed_lower, rng1))
                    dst_lower = mappings[mapping][map_]
                    rng2 = seed_range[1] - rng1
                    total_ranges.add((dst_lower, rng2))
                    hit = True
                elif map_lower <= seed_lower <= map_upper < seed_upper:
                    rng1 = seed_upper - map_upper
                    seeds_ranges.add((map_upper + 1, rng1))
                    dst_lower = mappings[mapping][map_]
                    offset_lower = seed_lower - map_lower
                    rng2 = seed_range[1] - rng1
                    total_ranges.add((dst_lower + offset_lower, rng2))
                    hit = True
                elif seed_lower < map_lower <= map_upper < seed_upper:
                    rng1 = map_lower - seed_lower
                    seeds_ranges.add((seed_lower, rng1))
                    rng2 = seed_upper - map_upper
                    seeds_ranges.add((map_upper + 1, rng2))
                    dst_lower = mappings[mapping][map_]
                    rng3 = map_[1]
                    total_ranges.add((dst_lower, rng3))
                    hit = True
            if not hit:
                total_ranges.add(seed_range)
        seeds_ranges = total_ranges

    print(min(seeds_ranges, key=lambda x: x[0])[0])


if __name__ == '__main__':
    main()
