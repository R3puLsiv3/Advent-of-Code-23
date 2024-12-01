
def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.split("\n")
    l1 = []
    occurs_in_l2 = {}
    for line in lines:
        values = line.split("   ")
        left = int(values[0])
        l1.append(left)
        if left not in occurs_in_l2:
            occurs_in_l2[left] = 0
        right = int(values[1])
        if right in occurs_in_l2:
            occurs_in_l2[right] += 1
        else:
            occurs_in_l2[right] = 1

    result = sum([x * occurs_in_l2[x] for x in l1])
    print(result)

if __name__ == '__main__':
    main()
