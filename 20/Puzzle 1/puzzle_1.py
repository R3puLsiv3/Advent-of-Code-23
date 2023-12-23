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

    low_pulses_sent = 0
    high_pulses_sent = 0
    for i in range(1000):
        module_queue = deque()
        low_pulses_sent += 1
        for module in modules["broadcaster"][0]:
            if module == "&":
                memory[module]["broadcaster"] = False
            else:
                incoming[module].append(False)
            module_queue.append(module)
        low_pulses_sent += len(modules["broadcaster"][0])

        while module_queue:
            module = module_queue.popleft()
            current_destinations = modules[module][0]
            current_type = modules[module][1]

            if current_type == "&":
                pulse = not all(list(memory[module].values()))
                for destination in current_destinations:
                    if destination not in modules:
                        continue
                    elif modules[destination][1] == "&":
                        memory[destination][module] = pulse
                    else:
                        incoming[destination].append(pulse)

                    module_queue.append(destination)

                if pulse:
                    high_pulses_sent += len(current_destinations)
                else:
                    low_pulses_sent += len(current_destinations)
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

                        module_queue.append(destination)

                    if pulse:
                        high_pulses_sent += len(current_destinations)
                    else:
                        low_pulses_sent += len(current_destinations)
                incoming[module].clear()

    print(low_pulses_sent * high_pulses_sent)


if __name__ == '__main__':
    main()
