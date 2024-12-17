def calculate_position(start_position, direction, distance):
    x_position = start_position[0] + direction[0] * distance
    y_position = start_position[1] + direction[1] * distance
    return x_position, y_position


def find_occurrences(starting_positions, letter_by_position):
    occurrences = 0
    for a_position in starting_positions:
        top_left_pos = calculate_position(a_position, (-1, 1), 1)
        top_right_pos = calculate_position(a_position, (1, 1), 1)
        bottom_left_pos = calculate_position(a_position, (-1, -1), 1)
        bottom_right_pos = calculate_position(a_position, (1, -1), 1)
        top_left_letter = letter_by_position.get(top_left_pos, "OOB")
        top_right_letter = letter_by_position.get(top_right_pos, "OOB")
        bottom_left_letter = letter_by_position.get(bottom_left_pos, "OOB")
        bottom_right_letter = letter_by_position.get(bottom_right_pos, "OOB")

        expected_letters = {"M", "S"}
        if {top_left_letter, bottom_right_letter} == expected_letters and {top_right_letter, bottom_left_letter} == expected_letters:
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
    result = find_occurrences(positions_by_letter["A"], letter_by_position)
    print(result)
    assert result == 1982


if __name__ == "__main__":
    main()
