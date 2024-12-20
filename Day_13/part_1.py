import re
from sympy import symbols, Eq, solve


class Button:
    def __init__(self, x: int, y: int, tokens: int):
        self.x = x
        self.y = y
        self.tokens = tokens


class Machine:
    def __init__(self, a: Button, b: Button, goal: (int, int)):
        self.a = a
        self.b = b
        self.goal = goal

    def calculate_position(self, a_presses, b_presses):
        return self.a.x * a_presses + self.b.x * b_presses, self.a.y * a_presses + self.b.y * b_presses

    def is_correct_position(self, position):
        return self.goal == position

    def calculate_tokens(self, a_presses, b_presses):
        return a_presses * self.a.tokens + b_presses * self.b.tokens


def read_input(filename):
    machines = []
    pattern = re.compile(r".*?:.*?X.(\d+).*?Y.(\d+)")

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            i = 0
            while i < len(lines) - 3:
                # Read Button A
                match_a = pattern.search(lines[i])
                if not match_a:
                    raise ValueError(f"Invalid format in line {i + 1}: {lines[i].strip()}")
                a_button = Button(int(match_a.group(1)), int(match_a.group(2)), 3)

                # Read Button B
                match_b = pattern.search(lines[i + 1])
                if not match_b:
                    raise ValueError(f"Invalid format in line {i + 2}: {lines[i + 1].strip()}")
                b_button = Button(int(match_b.group(1)), int(match_b.group(2)), 1)

                # Read Goal
                match_goal = pattern.search(lines[i + 2])
                if not match_goal:
                    raise ValueError(f"Invalid format in line {i + 3}: {lines[i + 2].strip()}")
                goal = (int(match_goal.group(1)), int(match_goal.group(2)))

                # Create a Machine object and add it to the list
                machine = Machine(a_button, b_button, goal)
                machines.append(machine)

                i += 4

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except ValueError as e:
        print(f"Error: {e}")

    return machines


def find_optimal_play(machine):
    A, B = symbols('A B')

    eq1 = Eq(machine.a.x * A + machine.b.x * B, machine.goal[0])
    eq2 = Eq(machine.a.y * A + machine.b.y * B, machine.goal[1])

    solution = solve((eq1, eq2), (A, B))
    if all(value.is_integer for value in solution.values()):
        a_presses, b_presses = solution[A], solution[B]
        return a_presses * machine.a.tokens + b_presses * machine.b.tokens
    else:
        return 0


def play_all(machines):
    optimal_tokens = 0
    for machine in machines:
        optimal_tokens += find_optimal_play(machine)
    return optimal_tokens


def main():
    filename = "input.txt"
    machines = read_input(filename)
    result = play_all(machines)
    print(result)
    assert result == 30973


if __name__ == "__main__":
    main()
