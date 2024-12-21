
def design_amount(dictionary, seen, design):
    if not design:
        return 1
    if design in seen:
        return seen[design]
    possibilities = 0
    for towel in dictionary[design[0]]:
        if design.startswith(towel):
            possibilities += design_amount(dictionary, seen, design[len(towel):])
    return possibilities

def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.split("\n")

    towels = lines[0].split(", ")
    designs = [line for line in lines[2:]]

    dictionary = {"w": [], "u": [], "b": [], "r": [], "g": []}
    for towel in towels:
        dictionary[towel[0]].append(towel)

    result = 0
    for design in designs:
        seen = {}
        for i in reversed(range(len(design))):
            suffix = design[i:]
            seen[suffix] = design_amount(dictionary, seen, suffix)
        result += seen[design]

    print(result)

if __name__ == '__main__':
    main()
