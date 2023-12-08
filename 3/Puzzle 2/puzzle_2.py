
def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.splitlines()
    line_length = (len(lines[0]) + 2)
    padded_data = "." * line_length
    for line in lines:
        padded_data += "." + line + "."
    padded_data += "." * line_length

    numbers = []
    current_number = ""
    for index, char in enumerate(padded_data):
        if char.isdigit():
            current_number += char
        elif current_number:
            numbers.append((current_number, index - len(current_number)))
            current_number = ""

    result = 0
    gear_pairs = {}
    for number in numbers:
        neighborhood = [(padded_data[number[1] - 1], number[1] - 1)]
        for i in range(len(number[0]) + 2):
            neighborhood.append((padded_data[number[1] - line_length + i - 1], number[1] - line_length + i - 1))
            neighborhood.append((padded_data[number[1] + line_length + i - 1], number[1] + line_length + i - 1))
        neighborhood.append((padded_data[number[1] + len(number[0])], number[1] + len(number[0])))

        for char in neighborhood:
            if char[0] == "*":
                if not char[1] in gear_pairs.keys():
                    gear_pairs[char[1]] = int(number[0])
                else:
                    result += gear_pairs[char[1]] * int(number[0])

    print(result)


if __name__ == '__main__':
    main()
