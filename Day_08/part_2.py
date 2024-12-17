def read_input(filename):
    positions_by_antenna = {}
    try:
        with open(filename, 'r') as file:
            i = 0
            for line in file:
                j = 0
                for antenna_type in line.strip():
                    if antenna_type != ".":
                        positions = positions_by_antenna.get(antenna_type, [])
                        positions.append((i, j))
                        positions_by_antenna[antenna_type] = positions
                    j += 1
                i += 1

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

    return positions_by_antenna


def is_valid_position(position):
    return 0 <= position[0] < 50 and 0 <= position[1] < 50


def calculate_position(origin, movement, times):
    return (origin[0] + movement[0] * times), (origin[1] + movement[1] * times)

def count_antinodes(positions_by_antenna):
    antinodes = set()
    for antenna, positions in positions_by_antenna.items():
        for i in range(len(positions)):
            for j in range(len(positions)):
                if i == j:
                    continue

                a = positions[i]                              # (42, 2)
                b = positions[j]                              # (44, 3)
                antinodes.add(a)
                antinodes.add(b)
                diff = (a[0] - b[0]), (a[1] - b[1])           # (-2, -1)

                a_prime = (a[0] + diff[0]), (a[1] + diff[1])  # (40, 1)
                while is_valid_position(a_prime):
                    antinodes.add(a_prime)
                    a_prime = (a_prime[0] + diff[0]), (a_prime[1] + diff[1])

                b_prime = (b[0] - diff[0]), (b[1] - diff[1])  # (46, 4)
                while is_valid_position(b_prime):
                    antinodes.add(b_prime)
                    b_prime = (b_prime[0] + diff[0]), (b_prime[1] + diff[1])

    return len(antinodes)


def main():
    filename = "input.txt"
    positions_by_antenna = read_input(filename)
    result = count_antinodes(positions_by_antenna)
    print(result)
    assert result == 861


if __name__ == "__main__":
    main()
