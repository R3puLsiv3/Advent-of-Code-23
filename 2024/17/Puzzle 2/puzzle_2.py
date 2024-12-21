def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.split("\n")
    program = list(map(int, lines[4][9:].split(",")))
    program_str = "".join(list(map(str, program)))

    counter = len(program)
    exp = 0
    exponents = []
    result = []
    seen = {}
    while counter:
        for i in range(8):
            # It turns out that for result r_0...r_m it holds that r_0*8^n + r_1*8^n-1 ... r_m*8^1 + i computes to the
            # suffix of length m + 1 of the desired string output. Since the desired output has length 16, this
            # algorithm ends after 16 steps and the result contains the solution as an octal number.
            r_a = i + sum([res * (8 ** exp) for res, exp in zip(result, reversed(exponents))])
            output = ""
            while r_a != 0:
                r_b = ((r_a % 8) ^ 4) ^ (r_a // (2 ** ((r_a % 8) ^ 1)))
                output += str(r_b % 8)
                r_a = r_a // 8
            if output not in seen:
                seen[output] = set()
            if program_str[len(program_str) - exp - 1:] == output and i not in seen[output]:
                result.append(i)
                exponents.append(exp + 1)
                seen[output].add(i)
                counter -= 1
                exp += 1
                break
            # Backtracking in case of dead end.
            if i == 7:
                counter += 1
                exp -= 1
                exponents.pop()
                result.pop()

    # Convert from octal to decimal.
    print(int("".join(map(str, result)), 8))

if __name__ == '__main__':
    main()