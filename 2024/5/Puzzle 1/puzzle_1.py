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

    allowed_updates = list(updates)
    for update in updates:
        not_allowed = set()
        for step in update:
            if step in not_allowed:
                allowed_updates.remove(update)
                break
            if step in rules_dict:
                not_allowed = not_allowed.union(rules_dict[step])

    result = sum([int(update[len(update) // 2]) for update in allowed_updates])
    print(result)

if __name__ == '__main__':
    main()
