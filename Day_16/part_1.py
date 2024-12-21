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


def dijkstra(maze, start, end):
    pq = []
    heapq.heappush(pq, (0, start, 0))  # (cost, position, direction_index)

    visited = {}  # { (position, direction_index): minimum_cost }

    while pq:
        cost, position, dir_index = heapq.heappop(pq)

        if position == end:
            return cost

        if (position, dir_index) in visited and visited[(position, dir_index)] <= cost:
            continue
        visited[(position, dir_index)] = cost

        x, y = position

        dx, dy = DIRECTIONS[dir_index]
        next_x, next_y = x + dx, y + dy
        if 0 <= next_y < len(maze) and 0 <= next_x < len(maze[0]) and maze[next_y][next_x] != '#':
            heapq.heappush(pq, (cost + 1, (next_x, next_y), dir_index))

        # Attempt to turn left or right (stay in the same position)
        left_dir = (dir_index - 1) % 4
        right_dir = (dir_index + 1) % 4
        heapq.heappush(pq, (cost + 1000, position, left_dir))
        heapq.heappush(pq, (cost + 1000, position, right_dir))

    return -1


def main():
    filename = "input.txt"
    maze, start, end = read_input(filename)
    result = dijkstra(maze, start, end)
    print(result)
    assert result == 82460


if __name__ == "__main__":
    main()
