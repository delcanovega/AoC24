def read_input(filename):
    topographic_map = [[-1] * 45 for _ in range(45)]
    trailheads = set()
    try:
        with open(filename, 'r') as file:
            i = 0
            for line in file:
                j = 0
                for pos in line.strip():
                    topographic_map[i][j] = int(pos)
                    if pos == "0":
                        trailheads.add((i, j))
                    j += 1
                i += 1

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

    return topographic_map, trailheads


def is_valid_movement(from_pos, to_pos, topographic_map):
    is_within_bounds = 0 <= to_pos[0] < 45 and 0 <= to_pos[1] < 45
    return is_within_bounds and topographic_map[to_pos[0]][to_pos[1]] - topographic_map[from_pos[0]][from_pos[1]] == 1


def dfs(topographic_map, current_pos, route, peaks_reached):
    if topographic_map[current_pos[0]][current_pos[1]] == 9:
        peaks_reached.add(current_pos)
        return

    movements = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for movement in movements:
        next_pos = (current_pos[0] + movement[0], current_pos[1] + movement[1])
        if next_pos not in route and is_valid_movement(current_pos, next_pos, topographic_map):
            route.add(next_pos)
            dfs(topographic_map, next_pos, route, peaks_reached)
            route.remove(next_pos)


def trace_route(topographic_map, trailhead):
    peaks_reached = set()
    dfs(topographic_map, trailhead, set(), peaks_reached)
    return len(peaks_reached)


def trace_routes(topographic_map, trailheads):
    total_score = 0
    for trailhead in trailheads:
        total_score += trace_route(topographic_map, trailhead)
    return total_score


def main():
    filename = "input.txt"
    topographic_map, trailheads = read_input(filename)
    result = trace_routes(topographic_map, trailheads)
    print(result)
    assert result == 557


if __name__ == "__main__":
    main()
