
def has_possibility(operands, result, current):
    # Slight speedup through pruning of the branches.
    if current > result:
        return False
    if not operands:
        return current == result
    next_operand = operands.pop()
    return has_possibility(list(operands), result, current + next_operand) or has_possibility(list(operands), result, current * next_operand) or has_possibility(list(operands), result, int(str(current)  + str(next_operand)))

def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.split("\n")
    operands_list = []
    results = []
    for line in lines:
        split_line = line.split(":")
        result = int(split_line[0])
        split_operands = list(reversed(list(map(int, split_line[1].strip().split(" ")))))
        operands_list.append(split_operands)
        results.append(result)

    sum_results = 0
    calibrations = zip(operands_list, results)
    for operands, result in calibrations:
        current = operands.pop()
        if has_possibility(operands, result, current):
            sum_results += result

    print(sum_results)

if __name__ == '__main__':
    main()
