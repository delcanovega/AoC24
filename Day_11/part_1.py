def read_input(filename):
    stones = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                for stone in line.strip().split(" "):
                    stones.append(int(stone))

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

    return stones


def blink(stones):
    i = 0
    while i < len(stones):
        stone_str = str(stones[i])
        if stones[i] == 0:
            stones[i] = 1
        elif len(stone_str) % 2 == 0:
            first, second = stone_str[:len(stone_str)//2], stone_str[len(stone_str)//2:]
            stones[i] = int(first)
            i += 1
            stones.insert(i, int(second))
        else:
            stones[i] *= 2024

        i += 1

    return stones


def observe(stones):
    for _ in range(25):
        #print(stones)
        blink(stones)
    return len(stones)


def main():
    filename = "input.txt"
    stones = read_input(filename)
    result = observe(stones)
    print(result)
    assert result == 185894


if __name__ == "__main__":
    main()
