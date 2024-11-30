
def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.splitlines()

    workflows = {}
    break_index = 0
    for index, line in enumerate(lines):
        if not line:
            break_index = index
            break
        curly_split = line[:-1].split("{")
        name = curly_split[0]
        rule_split = curly_split[1].split(",")

        rules = {}
        for rule in rule_split[:-1]:
            symbol = rule[0]
            compare = rule[1]
            compare_split = rule.split(compare)
            colon_split = compare_split[1].split(":")
            amount = int(colon_split[0])
            target = colon_split[1]
            rules[(symbol, compare, amount)] = target
        rules[("end", None, None)] = rule_split[-1]
        workflows[name] = rules

    parts = []
    for line in lines[break_index+1:]:
        category_split = line[1:-1].split(",")
        categories = {}
        for category in category_split:
            equal_split = category.split("=")
            name = equal_split[0]
            amount = int(equal_split[1])
            categories[name] = amount
        parts.append(categories)

    result = 0
    for part in parts:
        start_flow = "in"

        while True:
            for rule in workflows[start_flow]:
                if rule[0] == "end":
                    start_flow = workflows[start_flow][rule]
                    break
                elif rule[1] == "<":
                    if part[rule[0]] < rule[2]:
                        start_flow = workflows[start_flow][rule]
                        break
                    else:
                        continue
                else:
                    if part[rule[0]] > rule[2]:
                        start_flow = workflows[start_flow][rule]
                        break
                    else:
                        continue

            if start_flow == "A":
                result += part["x"] + part["m"] + part["a"] + part["s"]
                break
            elif start_flow == "R":
                break

    print(result)


if __name__ == '__main__':
    main()
