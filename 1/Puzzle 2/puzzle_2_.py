import re


def main():
    with open("input.txt") as f:
        data = f.read()

    data = data.replace("one", "one1one").replace("two", "two2two").replace("three", "three3three") \
        .replace("four", "four4four").replace("five", "five5five").replace("six", "six6six") \
        .replace("seven", "seven7seven").replace("eight", "eight8eight").replace("nine", "nine9nine")

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

