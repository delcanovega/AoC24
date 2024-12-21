from collections import deque

SIZE = 71

def read_input(filename):
    bytes_queue = deque()
    try:
        with open(filename, 'r') as file:
            for line in file.readlines():
                bytes_queue.append(list(map(int, line.strip().split(","))))
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

    return bytes_queue


def generate_grid(bytes_queue):
    grid = [["."] * SIZE for _ in range(SIZE)]
    for _ in range(1024):
        x, y = bytes_queue.popleft()
        grid[y][x] = "#"
    return grid


def find_shortest_path(grid):
    return bfs(grid, (0,0), (SIZE-1,SIZE-1))


def bfs(grid, pos, end):
    queue = deque([[pos]])
    visited = set()
    visited.add(pos)
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < SIZE and 0 <= ny < SIZE and grid[ny][nx] != "#" and (nx, ny) not in visited:
                new_path = list(path)
                new_path.append((nx, ny))
                queue.append(new_path)
                visited.add((nx, ny))
    return []


def main():
    filename = "input.txt"
    falling_bytes = read_input(filename)
    grid = generate_grid(falling_bytes)
    path = find_shortest_path(grid)
    result = len(path) - 1
    print(result)
    assert result == 384


if __name__ == "__main__":
    main()
