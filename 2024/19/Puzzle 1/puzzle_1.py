
def is_design_possible(dictionary, seen, design):
    if not design:
        return True
    elif design in seen:
        return False
    seen[design] = True
    possible = False
    for towel in dictionary[design[0]]:
        if design.startswith(towel):
            possible = possible or is_design_possible(dictionary, seen, design[len(towel):])
    return possible

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
        if is_design_possible(dictionary, seen, design):
            result += 1

    print(result)

if __name__ == '__main__':
    main()
