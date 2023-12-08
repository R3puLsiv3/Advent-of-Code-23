
def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.splitlines()

    result = 0
    for line in lines:
        colon_split = line.split(":")
        divider_split = colon_split[1].split("|")
        winning_numbers = divider_split[0].strip().split()
        my_numbers = divider_split[1].strip().split()

        winning_numbers_amount = {}
        for number in winning_numbers:
            winning_numbers_amount[number] = 0

        for number in my_numbers:
            if number in winning_numbers_amount:
                winning_numbers_amount[number] += 1

        matches = 0
        for number in winning_numbers_amount:
            if winning_numbers_amount[number] != 0:
                matches += 1

        if matches:
            result += 2 ** (matches - 1)

    print(result)


if __name__ == '__main__':
    main()
