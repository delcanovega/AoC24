from collections import deque

MAX_X = 100
MAX_Y = 50


def read_input(filename):
    boxxle = [["."] * MAX_X for _ in range(MAX_Y)]
    movements = ""
    robot = (0, 0)
    try:
        with open(filename, 'r') as file:
            input_str = file.read()
            map_part, movements_part = input_str.split("\n\n")
            i = 0
            for row in map_part.split("\n"):
                j = 0
                for col in row:
                    boxxle[i][j] = col
                    boxxle[i][j+1] = col
                    if col == "@":
                        robot = (j, i)
                        boxxle[i][j + 1] = "."
                    if col == "O":
                        boxxle[i][j] = "["
                        boxxle[i][j + 1] = "]"
                    j += 2
                i += 1

            movements = "".join(movements_part.split("\n"))

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

    return boxxle, movements, robot


def find_gap(boxxle, direction, robot):
    rx, ry = robot
    dx, _ = direction

    i = 1
    nx = rx + dx * i
    while 0 < nx < MAX_X - 1:
        if boxxle[ry][nx] == "#":
            return -1, -1
        if boxxle[ry][nx] == ".":
            return nx, ry

        i += 1
        nx = rx + dx * i

    return -1, -1


def dfs(boxxle, direction, initial_pos, segments_to_move, visited_positions):
    _, dy = direction

    pending_positions = deque([initial_pos])
    while pending_positions:
        rx, ry = pending_positions.popleft()
        if (rx, ry) in visited_positions:
            continue

        i = 1
        ny = ry + dy * i
        while 0 <= ny <= MAX_Y - 1:
            if boxxle[ny][rx] == "#":
                return False
            elif boxxle[ny][rx] == ".":
                segments_to_move.add(((rx, ny), (rx, ry)))
                break
            elif boxxle[ny][rx] == "[":
                visited_positions.add((rx, ny))
                if (rx + 1, ny) not in visited_positions:
                    pending_positions.append((rx + 1, ny))
            elif boxxle[ny][rx] == "]":
                visited_positions.add((rx, ny))
                if (rx - 1, ny) not in visited_positions:
                    pending_positions.append((rx - 1, ny))

            i += 1
            ny = ry + dy * i
    return True


def move_vertically(boxxle, direction, robot):
    segments_to_move = set()
    can_things_move = dfs(boxxle, direction, robot, segments_to_move, set())
    if can_things_move:
        for segment in segments_to_move:
            x, y = segment[0]
            tx, ty = segment[1]
            _, dy = direction
            while y != ty:
                boxxle[y][x] = boxxle[y - dy][x]
                y = y - dy
            boxxle[ty][tx] = "."
        return robot[0], robot[1] + direction[1]
    return robot


def simulate(boxxle, movements, robot):
    directions_by_input = {
        "^": (0, -1),
        "v": (0, 1),
        "<": (-1, 0),
        ">": (1, 0),
    }

    for move in movements:
        rx, ry = robot
        dx, dy = directions_by_input[move]
        if move in ["<", ">"]:
            x, y = find_gap(boxxle, (dx, dy), robot)
            if x != -1 and y != -1:
                i = x
                while i != rx:
                    boxxle[y][i] = boxxle[y][i - dx]
                    i -= dx
                boxxle[ry][rx] = "."
                robot = (rx + dx, ry)
        else:
            robot = move_vertically(boxxle, directions_by_input[move], robot)

        print(f"Move {move}:")
        for x in boxxle:
            print("".join(x))


def sum_boxes(boxxle):
    result = 0
    for y in range(MAX_Y):
        for x in range(MAX_X):
            if boxxle[y][x] == "[":
                result += x + 100 * y
    return result


def main():
    filename = "input.txt"
    boxxle, movements, robot = read_input(filename)
    simulate(boxxle, movements, robot)
    result = sum_boxes(boxxle)
    print(result)
    assert result == 1437981


if __name__ == "__main__":
    main()
