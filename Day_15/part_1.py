MAX_X = 50
MAX_Y = 50


def read_input(filename):
    boxxle = [["."] * MAX_X for _ in range(MAX_Y)]
    movements = ""
    robot = (0, 0)
    try:
        with open(filename, 'r') as file:
            input = file.read()
            map_part, movements_part = input.split("\n\n")
            x = 0
            for row in map_part.split("\n"):
                y = 0
                for col in row:
                    boxxle[x][y] = col
                    if (col == "@"):
                        robot = (x, y)
                    y += 1
                x += 1

            movements = "".join(movements_part.split("\n"))

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

    return boxxle, movements, robot


def find_gap(boxxle, direction, robot):
    rx, ry = robot
    dx, dy = direction

    i = 1
    nx = rx + dx * i
    ny = ry + dy * i
    while 0 < nx < MAX_X - 1 and 0 < ny < MAX_Y - 1:
        if boxxle[nx][ny] == "#":
            return -1, -1
        if boxxle[nx][ny] == ".":
            return nx, ny

        i += 1
        nx = rx + dx * i
        ny = ry + dy * i

    return -1, -1


def simulate(boxxle, movements, robot):
    directions_by_input = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1),
    }

    for move in movements:
        direction = directions_by_input[move]
        x, y = find_gap(boxxle, direction, robot)
        if x != -1 and y != -1:
            rx, ry = (robot[0] + direction[0], robot[1] + direction[1])
            boxxle[x][y] = "O"
            boxxle[rx][ry] = "@"
            boxxle[robot[0]][robot[1]] = "."
            robot = (rx, ry)

        #print(f"Move {move}:")
        #for x in boxxle:
        #    print("".join(x))


def sum_boxes(boxxle):
    result = 0
    for x in range(MAX_X):
        for y in range(MAX_Y):
            if boxxle[x][y] == "O":
                result += x * 100 + y
    return result


def main():
    filename = "input.txt"
    boxxle, movements, robot = read_input(filename)
    simulate(boxxle, movements, robot)
    result = sum_boxes(boxxle)
    print(result)
    assert result == 1438161


if __name__ == "__main__":
    main()
