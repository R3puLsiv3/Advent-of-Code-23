import numpy as np


def find_reflection(pattern, flipped, transposed, index, seen_positions):
    row_len = pattern.shape[0]
    for i in range(1, row_len // 2 + 1):
        pattern_upper = pattern[:i]
        pattern_lower = np.flip(pattern[i:i + i], axis=0)
        if np.array_equal(pattern_upper, pattern_lower) and not np.array_equal(pattern_upper, seen_positions[index]):
            if flipped and transposed:
                return row_len - i
            if not flipped and transposed:
                return i
            if flipped and not transposed:
                return (row_len - i) * 100
            else:
                return i * 100
    return 0


def find_seen_positions(pattern, index, seen_positions):
    row_len = pattern.shape[0]
    for i in range(1, row_len // 2 + 1):
        pattern_upper = pattern[:i]
        pattern_lower = np.flip(pattern[i:i + i], axis=0)
        if np.array_equal(pattern_upper, pattern_lower):
            seen_positions[index] = pattern_upper


def main():
    with open("input.txt") as f:
        data = f.read()

    data = data.replace(".", "0").replace("#", "1")
    lines = data.splitlines() + [""]

    patterns = []
    pattern = []
    for line in lines:
        if not line:
            pattern = np.array(pattern, dtype=int)
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(list(line))

    seen_positions = {}

    for index, pattern in enumerate(patterns):
        pattern_flipped = np.flip(pattern, axis=0)
        pattern_transposed = np.transpose(pattern)
        pattern_transposed_flipped = np.flip(pattern_transposed, axis=0)

        find_seen_positions(pattern, index, seen_positions)
        find_seen_positions(pattern_flipped, index, seen_positions)
        find_seen_positions(pattern_transposed, index, seen_positions)
        find_seen_positions(pattern_transposed_flipped, index, seen_positions)

    result = 0
    for index, pattern in enumerate(patterns):
        found = False
        for i in range(pattern.shape[0]):
            for j in range(pattern.shape[1]):
                if pattern[i, j]:
                    pattern[i, j] = 0
                else:
                    pattern[i, j] = 1
                pattern_flipped = np.flip(pattern, axis=0)
                pattern_transposed = np.transpose(pattern)
                pattern_transposed_flipped = np.flip(pattern_transposed, axis=0)

                value = 0
                value += find_reflection(pattern, False, False, index, seen_positions)
                value += find_reflection(pattern_flipped, True, False, index, seen_positions)
                value += find_reflection(pattern_transposed, False, True, index, seen_positions)
                value += find_reflection(pattern_transposed_flipped, True, True, index, seen_positions)
                if value:
                    result += value
                    found = True
                    break

                if pattern[i, j]:
                    pattern[i, j] = 0
                else:
                    pattern[i, j] = 1
            if found:
                break

    print(result)


if __name__ == '__main__':
    main()
