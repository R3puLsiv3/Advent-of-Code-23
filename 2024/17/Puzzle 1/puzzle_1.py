
def get_combo_value(operand, r_a, r_b, r_c):
    if operand <= 3:
        return operand
    elif operand == 4:
        return r_a
    elif operand == 5:
        return r_b
    elif operand == 6:
        return r_c

def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.split("\n")
    r_a = int(lines[0][12:])
    r_b = int(lines[1][12:])
    r_c = int(lines[2][12:])
    program = list(map(int, lines[4][9:].split(",")))

    instruction_pointer = 0
    outputs = []
    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]

        match opcode:
            case 0:
                value = get_combo_value(operand, r_a, r_b, r_c)
                r_a = r_a // (2 ** value)
            case 1:
                r_b = r_b ^ operand
            case 2:
                value = get_combo_value(operand, r_a, r_b, r_c)
                r_b = value % 8
            case 3:
                if r_a != 0:
                    instruction_pointer = operand
                    continue
            case 4:
                r_b = r_b ^ r_c
            case 5:
                value = get_combo_value(operand, r_a, r_b, r_c)
                output = value % 8
                outputs.append(str(output))
            case 6:
                value = get_combo_value(operand, r_a, r_b, r_c)
                r_b = r_a // (2 ** value)
            case 7:
                value = get_combo_value(operand, r_a, r_b, r_c)
                r_c = r_a // (2 ** value)
        instruction_pointer += 2

    print(",".join(outputs))

if __name__ == '__main__':
    main()
