import heapq

MAX_X = 141
MAX_Y = 141
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def read_input(filename):
    maze = [["."] * MAX_X for _ in range(MAX_Y)]
    start = (0, 0)
    end = (0, 0)
    try:
        with open(filename, 'r') as file:
            for y, row in enumerate(file.readlines()):
                for x, cell in enumerate(row.strip()):
                    maze[y][x] = cell
                    if cell == "S":
                        start = (x, y)
                    elif cell == "E":
                        end = (x, y)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

    return maze, start, end


def dijkstra_find_all_paths(maze, start, end):
    pq = []
    heapq.heappush(pq, (0, start, 0, [start]))  # (cost, position, direction_index, path)

    visited = {}  # { (position, direction_index): minimum_cost }
    paths_by_state = {}  # { (position, direction_index): [paths] }
    min_cost = 82460  # Prune all routes where cost exceeds our known minimum

    while pq:
        cost, position, dir_index, path = heapq.heappop(pq)

        # Stop processing paths that exceed the minimum cost
        if cost > min_cost:
            continue

        # If we reach the end, update the minimum cost and store the path
        if position == end:
            if cost == min_cost:
                paths = paths_by_state.get(end, [])
                paths.append(path)
                paths_by_state[end] = paths
            continue

        # Skip if this state has been visited with a cheaper cost
        if (position, dir_index) in visited and visited[(position, dir_index)] < cost:
            continue

        visited[(position, dir_index)] = cost

        # Save the current path for the state
        if (position, dir_index) not in paths_by_state:
            paths_by_state[(position, dir_index)] = []
        paths_by_state[(position, dir_index)].append(path)

        x, y = position

        # Attempt to move forward
        dx, dy = DIRECTIONS[dir_index]
        next_x, next_y = x + dx, y + dy
        if 0 <= next_y < len(maze) and 0 <= next_x < len(maze[0]) and maze[next_y][next_x] != '#':
            heapq.heappush(pq, (cost + 1, (next_x, next_y), dir_index, path + [(next_x, next_y)]))

        # Attempt to turn left or right
        left_dir = (dir_index - 1) % 4
        right_dir = (dir_index + 1) % 4
        heapq.heappush(pq, (cost + 1000, position, left_dir, path))
        heapq.heappush(pq, (cost + 1000, position, right_dir, path))

    print(min_cost)
    return paths_by_state.get(end, [])


def main():
    filename = "input.txt"
    maze, start, end = read_input(filename)
    optimal_paths = dijkstra_find_all_paths(maze, start, end)
    unique_positions = set()
    for path in optimal_paths:
        for position in path:
            unique_positions.add(position)
    result = len(unique_positions)
    print(result)
    assert result == 590


if __name__ == "__main__":
    main()
