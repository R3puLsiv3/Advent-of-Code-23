
class Block:
    def __init__(self, length, value):
        self.length = length
        self.value = value
        self.next = None
        self.prev = None
        self.done = False

def main():
    with open("input.txt") as f:
        data = f.read()

    block = Block(0, 0)
    head = block

    counter = 0
    for i, char in enumerate(data):
        if i % 2 == 0:
            new_block = Block(int(char), counter)
            block.next = new_block
            new_block.prev = block
            block = new_block
            counter += 1
        else:
            new_block = Block(int(char), -1)
            block.next = new_block
            new_block.prev = block
            block = new_block
    block.next = head
    head.prev = block

    block = head.prev
    while block != head:
        if block.done:
            block = block.prev
            continue

        prev_block = block.prev

        if block.value != -1:
            check_block = head.next
            while (check_block.length < block.length or check_block.value != -1) and check_block != block:
                check_block = check_block.next

            if check_block != block:
                check_block.length -= block.length

                new_block = Block(block.length, block.value)
                check_block.prev.next = new_block
                new_block.prev = check_block.prev
                new_block.next = check_block
                check_block.prev = new_block

                block.value = -1

        block.done = True
        block = prev_block

    block = head.next
    representation = []
    while block != head:
        for i in range(block.length):
            representation.append(block.value)
        block = block.next

    counter = 0
    result = 0
    for num in representation:
        if num != -1:
            result += num * counter
        counter += 1

    print(result)

if __name__ == '__main__':
    main()
