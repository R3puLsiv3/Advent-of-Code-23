import math
from collections import deque


def main():
    with open("input.txt") as f:
        data = f.read()

    data = data.replace(" ", "")
    lines = data.splitlines()

    modules = {}
    memory = {}
    ff_state = {}
    incoming = {}
    for line in lines:
        arrow_split = line.split("->")
        destinations = arrow_split[1].split(",")
        if arrow_split[0] == "broadcaster":
            modules["broadcaster"] = (destinations, "broadcaster")
        else:
            module_type = arrow_split[0][0]
            module_name = arrow_split[0][1:]
            modules[module_name] = (destinations, module_type)
            if module_type == "&":
                memory[module_name] = {}
            elif module_type == "%":
                ff_state[module_name] = False
                incoming[module_name] = []

    for module in modules:
        for destination in modules[module][0]:
            if destination in modules and modules[destination][1] == "&":
                memory[destination][module] = False

    found = False
    index = 0
    rk_index = index
    rk_found = False
    cd_index = index
    cd_found = False
    zf_index = index
    zf_found = False
    qx_index = index
    qx_found = False
    while True:
        index += 1

        if rk_found and cd_found and zf_found and qx_found:
            break
        module_queue = deque()
        for module in modules["broadcaster"][0]:
            if module == "&":
                memory[module]["broadcaster"] = False
            else:
                incoming[module].append(False)
            module_queue.append(module)

        while module_queue:
            if found:
                break
            module = module_queue.popleft()
            current_destinations = modules[module][0]
            current_type = modules[module][1]

            # By checking input I see that gh has to receive a high pulse from all of these to send a low pulse to rx
            # I check the first occurrence of a high pulse for each one and calculate the least common multiple
            if module == "gh" and memory["gh"]["rk"]:
                rk_index = index
                rk_found = True
            if module == "gh" and memory["gh"]["cd"]:
                cd_index = index
                cd_found = True
            if module == "gh" and memory["gh"]["zf"]:
                zf_index = index
                zf_found = True
            if module == "gh" and memory["gh"]["qx"]:
                qx_index = index
                qx_found = True

            if current_type == "&":
                pulse = not all(list(memory[module].values()))
                for destination in current_destinations:
                    if destination not in modules:
                        continue
                    elif modules[destination][1] == "&":
                        memory[destination][module] = pulse
                    else:
                        incoming[destination].append(pulse)

                    if destination == "rx" and not pulse:
                        found = True
                        break
                    module_queue.append(destination)

            elif current_type == "%":
                pulse = any(not signal for signal in incoming[module])
                if pulse:
                    if ff_state[module]:
                        ff_state[module] = False
                        pulse = False
                    else:
                        ff_state[module] = True
                        pulse = True
                    for destination in current_destinations:
                        if destination not in modules:
                            continue
                        elif modules[destination][1] == "&":
                            memory[destination][module] = pulse
                        else:
                            incoming[destination].append(pulse)

                        if destination == "rx" and not pulse:
                            found = True
                            break
                        module_queue.append(destination)

                incoming[module].clear()

    print(math.lcm(*[rk_index, cd_index, zf_index, qx_index]))


if __name__ == '__main__':
    main()
