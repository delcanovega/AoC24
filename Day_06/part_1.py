def read_input(filename):
    guard_map = [[" "] * 130 for _ in range(130)]
    init_pos = ()
    try:
        with open(filename, 'r') as file:
            i = 0
            for line in file:
                j = 0
                for pos in line.strip():
                    guard_map[i][j] = pos
                    if pos == "^":
                        guard_map[i][j] = "X"
                        init_pos = (i, j)
                    j += 1
                i += 1

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

    return guard_map, init_pos


def is_guard_gone(current_pos):
    return current_pos[0] < 0 or current_pos[0] >= 130 or current_pos[1] < 0 or current_pos[1] >= 130

def trace_route(guard_map, init_pos):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_direction_idx = 0

    current_position = init_pos
    while not is_guard_gone(current_position):
        next_position = (current_position[0] + directions[current_direction_idx][0], current_position[1] + directions[current_direction_idx][1])
        if is_guard_gone(next_position):
            break
        elif guard_map[next_position[0]][next_position[1]] == "#":
            current_direction_idx = (current_direction_idx + 1) % len(directions)
        else:
            guard_map[next_position[0]][next_position[1]] = "X"
            current_position = next_position

    result = 0
    for row in guard_map:
        print("".join(row))
        for cell in row:
            if cell == "X":
                result += 1
    return result

def main():
    filename = "input.txt"
    guard_map, init_pos = read_input(filename)
    result = trace_route(guard_map, init_pos)
    print(result)
    assert result == 5239


if __name__ == "__main__":
    main()
