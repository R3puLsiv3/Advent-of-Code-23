
def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.splitlines()

    cards = {}
    for game, line in enumerate(lines):
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

        amount = 1
        cards[game + 1] = {"amount": amount, "matches": matches}

    total_cards = 0
    for number, data in cards.items():
        total_cards += data["amount"]

        for j in range(data["matches"]):
            cards[number + j + 1]["amount"] += data["amount"]

    print(total_cards)


if __name__ == '__main__':
    main()
