import numpy as np
import re

def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.split("\n")

    buttons_list = []
    targets = []
    a_x = 0
    a_y = 0
    b_x = 0
    b_y = 0
    target_x = 0
    target_y = 0
    for line in lines:
        if line == "":
            buttons_list.append(np.array([[a_x, b_x], [a_y, b_y]], dtype=np.int64))
            targets.append(np.array([target_x, target_y], dtype=np.int64))
        elif match := re.search("Button ([AB]): X\+(\d+), Y\+(\d+)", line):
            if match.group(1) == "A":
                a_x = match.group(2)
                a_y = match.group(3)
            else:
                b_x = match.group(2)
                b_y = match.group(3)
        else:
            match = re.search("Prize: X=(\d+), Y=(\d+)", line)
            target_x = 10000000000000 + int(match.group(1))
            target_y = 10000000000000 + int(match.group(2))
    buttons_list.append(np.array([[a_x, b_x], [a_y, b_y]], dtype=np.int64))
    targets.append(np.array([target_x, target_y], dtype=np.int64))

    result = 0
    for buttons, target in zip(buttons_list, targets):
        presses = np.linalg.inv(buttons).dot(target)
        press_x = presses[0]
        press_y = presses[1]
        cost_presses = 0
        if np.isclose(press_x, np.round(press_x), atol=0.01, rtol=0) and np.isclose(press_y, np.round(press_y), atol=0.01, rtol=0):
            cost_presses = int(round(3 * press_x + press_y))
        result += cost_presses

    print(result)

if __name__ == '__main__':
    main()
