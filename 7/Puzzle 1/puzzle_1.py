
def main():
    with open("input.txt") as f:
        data = f.read()

    data = data.replace("A", "e").replace("K", "d").replace("Q", "c").replace("J", "b").replace("T", "a")
    lines = data.splitlines()

    data = []
    for line in lines:
        hand_and_bid = tuple(line.split())
        data.append(hand_and_bid)

    types = {"five_of_a_kind": [], "four_of_a_kind": [], "full_house": [], "three_of_a_kind": [], "two_pair": [],
             "one_pair": [], "high_card": []}

    for hand_and_bid in data:
        kinds = {"e": 0, "d": 0, "c": 0, "b": 0, "a": 0, "9": 0, "8": 0, "7": 0, "6": 0, "5": 0, "4": 0, "3": 0, "2": 0}
        for char in hand_and_bid[0]:
            kinds[char] += 1

        got_3 = False
        got_2 = False
        done = False
        for kind in kinds:
            match kinds[kind]:
                case 5:
                    types["five_of_a_kind"].append(hand_and_bid)
                    done = True
                    break
                case 4:
                    types["four_of_a_kind"].append(hand_and_bid)
                    done = True
                    break
                case 3:
                    if got_2:
                        types["full_house"].append(hand_and_bid)
                        done = True
                        break
                    got_3 = True
                    continue
                case 2:
                    if got_2:
                        types["two_pair"].append(hand_and_bid)
                        done = True
                        break
                    got_2 = True
                    if got_3:
                        types["full_house"].append(hand_and_bid)
                        done = True
                        break
                    continue
                case _:
                    continue

        if got_2 and not done:
            types["one_pair"].append(hand_and_bid)
        elif got_3 and not done:
            types["three_of_a_kind"].append(hand_and_bid)
        elif not done:
            types["high_card"].append(hand_and_bid)

    sorted_list = []
    for type_ in types:
        types[type_].sort(reverse=True)
        sorted_list += types[type_]
    sorted_list.reverse()

    result = 0
    for index, hand in enumerate(sorted_list):
        result += (index + 1) * int(hand[1])

    print(result)


if __name__ == '__main__':
    main()
