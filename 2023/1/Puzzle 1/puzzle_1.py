import re


def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.split("\n")

    result = 0
    for line in lines:
        if re.fullmatch("[a-z]*([1-9]).*([1-9])[a-z]*", line):
            line = int(re.sub("[a-z]*([1-9]).*([1-9])[a-z]*", "\\1\\2", line))
        else:
            line = int(re.sub("[a-z]*([1-9])[a-z]*", "\\1\\1", line))
        result += line

    print(result)


if __name__ == '__main__':
    main()

