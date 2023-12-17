
def main():
    with open("input.txt") as f:
        data = f.read()

    split_data = data.split(",")
    steps = []
    for string in split_data:
        step = []
        for char in string:
            step.append(char)
        steps.append(step)

    boxes = {}
    for i in range(256):
        boxes[i] = {}

    result = 0
    for step in steps:
        current_value = 0
        current_lens = ""
        for char in step:
            if char.isalpha():
                current_value += ord(char)
                current_lens += char
                current_value *= 17
                current_value %= 256
            elif char == "-":
                current_box = current_value
                if current_lens in boxes[current_box]:
                    del boxes[current_box][current_lens]
            else:
                current_box = current_value
                focal_length = int(step[-1])
                boxes[current_box][current_lens] = focal_length

    for box in boxes:
        slot_number = 1
        for lens in boxes[box]:
            result += (box + 1) * slot_number * boxes[box][lens]
            slot_number += 1

    print(result)


if __name__ == '__main__':
    main()
