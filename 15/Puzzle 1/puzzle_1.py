
def main():
    with open("input.txt") as f:
        data = f.read()

    split_data = data.split(",")
    to_hash = []
    for string in split_data:
        ascii_values = []
        for char in string:
            ascii_values.append(ord(char))
        to_hash.append(ascii_values)

    result = 0
    for numbers in to_hash:
        current_value = 0
        for number in numbers:
            current_value += number
            current_value *= 17
            current_value %= 256
        result += current_value

    print(result)


if __name__ == '__main__':
    main()
