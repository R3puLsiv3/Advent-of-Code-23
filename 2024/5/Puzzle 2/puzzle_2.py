import itertools

def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.split("\n")
    rules = [tuple(rule.split("|")) for rule in itertools.takewhile(lambda x: x != "", lines)]
    updates = [update.split(",") for update in itertools.dropwhile(lambda x: x != "", lines) if update != ""]

    rules_dict = {}
    for (before, after) in rules:
        if after in rules_dict:
            rules_dict[after].add(before)
        else:
            rules_dict[after] = {before}

    not_allowed_updates = []
    for update in updates:
        not_allowed = set()
        for step in update:
            if step in not_allowed:
                not_allowed_updates.append(update)
                break
            if step in rules_dict:
                not_allowed = not_allowed.union(rules_dict[step])

    # Calculate depths of the elements of each update in the quasi tree rules_dict.
    fixed_updates = []
    for update in not_allowed_updates:
        depth = {step: 0 for step in update}
        for step1 in update:
            for step2 in update:
                if step2 in rules_dict[step1]:
                    depth[step1] += 1

        fixed_updates.append([step for (step, _) in sorted(depth.items(), key=lambda item: item[1])])

    result = sum([int(update[len(update) // 2]) for update in fixed_updates])
    print(result)

if __name__ == '__main__':
    main()
