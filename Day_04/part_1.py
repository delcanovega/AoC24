def calculate_position(start_position, direction, distance):
    x_position = start_position[0] + direction[0] * distance
    y_position = start_position[1] + direction[1] * distance
    return x_position, y_position


def find_occurrences(starting_positions, letter_by_position):
    occurrences = 0
    direction_vectors = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    for x_position in starting_positions:
        for current_direction in direction_vectors:
            distance = 1
            for expected_letter in "MAS":
                position_to_check = calculate_position(x_position, current_direction, distance)
                distance += 1
                if letter_by_position.get(position_to_check, "OOB") != expected_letter:
                    break
                elif expected_letter == "S":
                    occurrences += 1
    return occurrences


def read_input(filename):
    positions_by_letter = {}
    letter_by_position = {}

    try:
        with open(filename, 'r') as file:
            x = 0
            y = 0
            for line in file:
                chars = line.strip()
                for char in chars:
                    position = (x, y)
                    positions = positions_by_letter.get(char, [])
                    positions.append(position)
                    positions_by_letter[char] = positions
                    letter_by_position[position] = char
                    x += 1
                x = 0
                y += 1

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

    return positions_by_letter, letter_by_position


def main():
    filename = "input.txt"
    positions_by_letter, letter_by_position = read_input(filename)
    result = find_occurrences(positions_by_letter["X"], letter_by_position)
    print(result)
    assert result == 2464


if __name__ == "__main__":
    main()
