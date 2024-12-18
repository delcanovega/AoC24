def read_input(filename):
    stones_by_number = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                for stone in line.strip().split(" "):
                    stones = stones_by_number.get(int(stone), 0)
                    stones += 1
                    stones_by_number[int(stone)] = stones

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

    return stones_by_number


def increase_stones(stones_by_number, stone_number, stone_amount):
    existing_stones = stones_by_number.get(stone_number, 0)
    existing_stones += stone_amount
    stones_by_number[stone_number] = existing_stones


def blink(stones_by_number):
    new_stones_by_number = {}
    for number, stone_amount in stones_by_number.items():
        number_str = str(number)
        if number == 0:
            increase_stones(new_stones_by_number, 1, stone_amount)
        elif len(number_str) % 2 == 0:
            first, second = number_str[:len(number_str) // 2], number_str[len(number_str) // 2:]
            increase_stones(new_stones_by_number, int(first), stone_amount)
            increase_stones(new_stones_by_number, int(second), stone_amount)
        else:
            increase_stones(new_stones_by_number, number * 2024, stone_amount)

    return new_stones_by_number


def observe(stones_by_number):
    for _ in range(75):
        stones_by_number = blink(stones_by_number)

    return sum(stones_by_number.values())


def main():
    filename = "input.txt"
    stones_by_number = read_input(filename)
    result = observe(stones_by_number)
    print(result)
    assert result == 221632504974231


if __name__ == "__main__":
    main()
