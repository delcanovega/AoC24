import re

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


def get_quadrant(position):
    x, y = position
    if 0 <= x < MAX_X // 2 and 0 <= y < MAX_Y // 2:
        return 0
    elif MAX_X // 2 < x < MAX_X and 0 <= y < MAX_Y // 2:
        return 1
    elif 0 <= x < MAX_X // 2 and MAX_Y // 2 < y < MAX_Y:
        return 2
    elif MAX_X // 2 < x < MAX_X and MAX_Y // 2 < y < MAX_Y:
        return 3
    else:
        return 4


def calculate_safety_factor(positions):
    robots_by_quadrant = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
    }

    for position in positions:
        quadrant = get_quadrant(position)
        robots_by_quadrant[quadrant] += 1

    return robots_by_quadrant[0] * robots_by_quadrant[1] * robots_by_quadrant[2] * robots_by_quadrant[3]


def main():
    filename = "input.txt"
    robots = read_input(filename)
    future_positions = simulate(robots, 100)
    result = calculate_safety_factor(future_positions)
    print(result)
    assert result == 225521010


if __name__ == "__main__":
    main()
