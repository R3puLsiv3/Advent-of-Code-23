
def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.splitlines()

    sequences = []
    for line in lines:
        sequences.append([int(x) for x in line.split()])

    result = 0
    for sequence in sequences:
        length = len(sequence) - 1
        while not all(number == 0 for number in sequence[:length]):
            for index in range(length):
                sequence[index] = sequence[index + 1] - sequence[index]
            length -= 1
        result += sum(sequence)

    print(result)


if __name__ == '__main__':
    main()
