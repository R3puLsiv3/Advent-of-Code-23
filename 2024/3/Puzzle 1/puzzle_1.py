import re

def main():
    with open("input.txt") as f:
        data = f.read()

    mul_pattern = re.compile("mul\(([0-9]{1,3}),([0-9]{1,3})\)")
    result_strings = re.findall(mul_pattern, data)

    result = sum(map(lambda a: int(a[0]) * int(a[1]), result_strings))
    print(result)

if __name__ == '__main__':
    main()
