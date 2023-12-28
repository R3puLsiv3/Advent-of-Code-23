
def find_combinations(intervals, workflow, workflows):
    if workflow == "A":
        return (intervals["x"][1] - intervals["x"][0] + 1) * (intervals["m"][1] - intervals["m"][0] + 1) *\
               (intervals["a"][1] - intervals["a"][0] + 1) * (intervals["s"][1] - intervals["s"][0] + 1)
    elif workflow == "R":
        return 0

    result = 0
    for rule in workflows[workflow]:
        symbol = rule[0]
        compare = rule[1]
        bound = rule[2]

        if symbol == "end":
            new_workflow = workflows[workflow][rule]
            result += find_combinations(dict(intervals), new_workflow, workflows)
            break

        lower = intervals[symbol][0]
        upper = intervals[symbol][1]

        if compare == "<":
            if bound <= lower:
                continue
            elif upper < bound:
                new_workflow = workflows[workflow][rule]
                result += find_combinations(dict(intervals), new_workflow, workflows)
            else:
                new_workflow = workflows[workflow][rule]
                new_intervals = dict(intervals)
                new_intervals[symbol] = [lower, bound - 1]
                result += find_combinations(new_intervals, new_workflow, workflows)
                intervals[symbol] = [bound, upper]
                continue
        else:
            if upper <= bound:
                continue
            elif lower > bound:
                new_workflow = workflows[workflow][rule]
                result += find_combinations(dict(intervals), new_workflow, workflows)
            else:
                new_workflow = workflows[workflow][rule]
                new_intervals = dict(intervals)
                new_intervals[symbol] = [bound + 1, upper]
                result += find_combinations(new_intervals, new_workflow, workflows)
                intervals[symbol] = [lower, bound]
                continue
    return result


def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.splitlines()

    workflows = {}
    for line in lines:
        if not line:
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

    start_intervals = {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}
    start_workflow = "in"
    result = find_combinations(start_intervals, start_workflow, workflows)

    print(result)


if __name__ == '__main__':
    main()
