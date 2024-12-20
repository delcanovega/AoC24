import re
from collections import deque

MAX_X = 101
MAX_Y = 103

class Robot:
    def __init__(self, initial_x, initial_y, dx, dy):
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.dx = dx
        self.dy = dy

    def calculate_position(self, t):
        return (self.initial_x + self.dx * t) % MAX_X, (self.initial_y + self.dy * t) % MAX_Y


def read_input(filename):
    robots = []
    pattern = r"-?\d+"
    try:
        with open(filename, 'r') as file:
            for line in file.readlines():
                matches = re.findall(pattern, line)
                matches = list(map(int, matches))
                robots.append(Robot(matches[0], matches[1], matches[2], matches[3]))

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

    return robots


def simulate(robots, t):
    return[ robot.calculate_position(t) for robot in robots ]


def plot(positions, canvas):
    for y, x in positions:
        canvas[x][y] = "#"


def has_suspicious_group(positions):
    points_set = set(positions)
    groups = []

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def bfs(pos):
        queue = deque([pos])
        cluster = []

        while queue:
            x, y = queue.popleft()
            if (x, y) in points_set:
                points_set.remove((x, y))
                cluster.append((x, y))

                for dx, dy in directions:
                    neighbor = (x + dx, y + dy)
                    if neighbor in points_set:
                        queue.append(neighbor)

        return cluster

    while points_set:
        initial_pos = next(iter(points_set))
        group = bfs(initial_pos)
        groups.append(group)

    threshold = 50
    return any([len(group) > threshold for group in groups])


def art_attack(robots):
    for i in range(10000):
        canvas = [["."] * MAX_X for _ in range(MAX_Y)]
        positions = simulate(robots, i)
        if has_suspicious_group(positions):
            plot(positions, canvas)
            print(f"=========")
            for row in range(MAX_X):
                print("".join(canvas[row]))
            print(f"that was iteration: {i}")


def main():
    filename = "input.txt"
    robots = read_input(filename)
    art_attack(robots)
    # This one requires manual inspection. Solution found at iteration 7774


if __name__ == "__main__":
    main()
