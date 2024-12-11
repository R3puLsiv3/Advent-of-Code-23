
def main():
    with open("input.txt") as f:
        data = f.read()
    data = data.split(" ")

    occurrences = {}
    for num in data:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1

    for i in range(75):
        new_occurrences = {}
        for num in occurrences.keys():
            if num == "0":
                if "1" in new_occurrences:
                    new_occurrences["1"] += occurrences["0"]
                else:
                    new_occurrences["1"] = occurrences["0"]
            elif (length := len(num)) % 2 == 0:
                left = num[:length // 2]
                right = str(int(num[length // 2:]))
                if left in new_occurrences:
                    new_occurrences[left] += occurrences[num]
                else:
                    new_occurrences[left] = occurrences[num]
                if right in new_occurrences:
                    new_occurrences[right] += occurrences[num]
                else:
                    new_occurrences[right] = occurrences[num]
            else:
                product = str(int(num) * 2024)
                if product in new_occurrences:
                    new_occurrences[product] += occurrences[num]
                else:
                    new_occurrences[product] = occurrences[num]
        occurrences = new_occurrences

    print(sum(occurrences.values()))


if __name__ == '__main__':
    main()
