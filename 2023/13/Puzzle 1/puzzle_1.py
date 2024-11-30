import numpy as np


def find_reflection(pattern, flipped, transposed):
    row_len = pattern.shape[0]
    for i in range(1, row_len // 2 + 1):
        pattern_upper = pattern[:i]
        pattern_lower = np.flip(pattern[i:i + i], axis=0)
        if np.array_equal(pattern_upper, pattern_lower):
            if flipped and transposed:
                return row_len - i
            if not flipped and transposed:
                return i
            if flipped and not transposed:
                return (row_len - i) * 100
            else:
                return i * 100
    return 0


def main():
    with open("input.txt") as f:
        data = f.read()

    data = data.replace(".", "0").replace("#", "1")
    lines = data.splitlines() + ["", ""]

    patterns = []
    pattern = []
    for line in lines:
        if not line:
            pattern = np.array(pattern, dtype=int)
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(list(line))

    result = 0

    for pattern in patterns:
        pattern_flipped = np.flip(pattern, axis=0)
        pattern_transposed = np.transpose(pattern)
        pattern_transposed_flipped = np.flip(pattern_transposed, axis=0)

        result += find_reflection(pattern, False, False)
        result += find_reflection(pattern_flipped, True, False)
        result += find_reflection(pattern_transposed, False, True)
        result += find_reflection(pattern_transposed_flipped, True, True)

    print(result)


if __name__ == '__main__':
    main()
