
def main():
    with open("input.txt") as f:
        data = f.read()

    counter = 0
    empty_count = 0
    representation = []
    for i, char in enumerate(data):
        if i % 2 == 0:
            for j in range(int(char)):
                representation.append(counter)
            counter += 1
        else:
            for j in range(int(char)):
                representation.append(-1)
                empty_count += 1

    pos = 0
    while empty_count:
        current = representation.pop()
        if current == -1:
            empty_count -= 1
            continue
        else:
            while representation[pos] != -1:
                pos += 1
            representation[pos] = current
            empty_count -= 1

    counter = 0
    result = 0
    for num in representation:
        result += num * counter
        counter += 1

    print(result)

if __name__ == '__main__':
    main()
