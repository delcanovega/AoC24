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

def is_guard_stuck_in_loop(guard_map, init_pos):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_direction_idx = 0

    current_position = init_pos
    hits = set()
    while not is_guard_gone(current_position):
        next_position = (current_position[0] + directions[current_direction_idx][0], current_position[1] + directions[current_direction_idx][1])
        if is_guard_gone(next_position):
            return False
        elif guard_map[next_position[0]][next_position[1]] == "#":
            pos = (next_position[0], next_position[1], current_direction_idx)
            if pos in hits:
                return True
            else:
                hits.add(pos)
                current_direction_idx = (current_direction_idx + 1) % len(directions)
        else:
            current_position = next_position


def try_all_options(guard_map, init_pos):
    valid_options = 0
    for i in range(130):
        for j in range(130):
            if guard_map[i][j] == ".":
                guard_map[i][j] = "#"
                print(f"{i}:{j}")
                if is_guard_stuck_in_loop(guard_map, init_pos):
                    valid_options += 1
                guard_map[i][j] = "."
    return valid_options


def main():
    filename = "input.txt"
    guard_map, init_pos = read_input(filename)
    result = try_all_options(guard_map, init_pos)
    print(result)
    assert result == 1753


if __name__ == "__main__":
    main()
