from collections import deque


def read_input(filename):
    crop_map = [["."] * 140 for _ in range(140)]
    try:
        with open(filename, 'r') as file:
            i = 0
            for line in file:
                j = 0
                for crop in line.strip():
                    crop_map[i][j] = crop
                    j += 1
                i += 1

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

    return crop_map


def is_fence_needed(crop_map, crop, pos_to_check):
    rows = len(crop_map)
    cols = len(crop_map[0])
    is_oob = pos_to_check[0] < 0 or pos_to_check[0] >= rows or pos_to_check[1] < 0 or pos_to_check[1] >= cols
    return is_oob or crop_map[pos_to_check[0]][pos_to_check[1]] != crop


def calculate_fences(crop_map, position, crop):
    fences_needed = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for direction in directions:
        pos_to_check = (position[0] + direction[0], position[1] + direction[1])
        if is_fence_needed(crop_map, crop, pos_to_check):
            fences_needed += 1

    return fences_needed


def calculate_price(crop_map, regions):
    price = 0
    for region in regions:
        crop = region[0]
        positions = region[1]
        fences = sum(list(map(lambda pos : calculate_fences(crop_map, pos, crop), positions)))
        price += fences * len(region[1])

    return price


def divide_into_regions(crop_map):
    rows = len(crop_map)
    cols = len(crop_map[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    regions = []

    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def bfs(row, col):
        queue = deque([(row, col)])
        visited[row][col] = True
        crop = crop_map[row][col]
        positions = [(row, col)]

        while queue:
            x, y = queue.popleft()
            for dx, dy in movements:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and crop_map[nx][ny] == crop:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    positions.append((nx, ny))

        return positions

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                positions = bfs(i, j)
                regions.append((crop_map[i][j], positions))

    return regions


def main():
    filename = "input.txt"
    crop_map = read_input(filename)
    regions = divide_into_regions(crop_map)
    result = calculate_price(crop_map, regions)
    print(result)
    assert result == 1400386


if __name__ == "__main__":
    main()
