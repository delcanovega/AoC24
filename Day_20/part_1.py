from collections import deque

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


def bfs(maze, start, end, best_length):
    queue = deque([[start]])
    visited = set()
    visited.add(start)
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        if len(path) > best_length:
            continue

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < MAX_X and 0 <= ny < MAX_Y and maze[ny][nx] != "#" and (nx, ny) not in visited:
                new_path = list(path)
                new_path.append((nx, ny))
                queue.append(new_path)
                visited.add((nx, ny))
    return []


def is_potential_shortcut(pos, maze):
    x, y = pos
    if maze[y][x] == "#":
        fx, tx= x - 1, x + 1
        if 0 < fx < MAX_X and maze[y][fx] != "#" and 0 < tx < MAX_X and maze[y][tx] != "#":
            return True
        fy, ty = y - 1, y + 1
        if 0 < fy < MAX_Y and maze[fy][x] != "#" and 0 < ty < MAX_Y and maze[ty][x] != "#":
            return True
    return False


def find_potential_shortcuts(maze):
    potential_shortcuts = []
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if is_potential_shortcut((x, y), maze):
                potential_shortcuts.append((x, y))
    return potential_shortcuts


def test_shortcuts(maze, start, end, best_path, potential_shortcuts):
    valid_shortcuts = []
    for x, y in potential_shortcuts:
        maze[y][x] = "."
        result = bfs(maze, start, end, len(best_path) - 100)
        if result:
            valid_shortcuts.append((x, y))
        maze[y][x] = "#"
    return valid_shortcuts


def main():
    filename = "input.txt"
    maze, start, end = read_input(filename)
    shortest_path = bfs(maze, start, end, 9999)
    potential_shortcuts = find_potential_shortcuts(maze)
    valid_shortcuts = test_shortcuts(maze, start, end, shortest_path, potential_shortcuts)
    result = len(valid_shortcuts)
    print(result)
    assert result == 1402


if __name__ == "__main__":
    main()
