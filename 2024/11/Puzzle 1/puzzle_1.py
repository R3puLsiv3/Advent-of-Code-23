
def main():
    with open("input.txt") as f:
        data = f.read()
    data = data.split(" ")

    for _ in range(25):
        new_data = []

        occurrences = {}
        for num in data:
            if num in occurrences:
                occurrences[num] += 1
            else:
                occurrences[num] = 1

        for num in data:
            if num == "0":
                new_data.append("1")
            elif (length := len(num)) % 2 == 0:
                new_data.append(num[:length // 2])
                new_data.append(str(int(num[length // 2:])))
            else:
                new_data.append(str(int(num) * 2024))
        data = new_data

    print(len(data))

if __name__ == '__main__':
    main()
