def read_input(filename):
    equations = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                left, right = line.split(":")
                result = int(left)
                operands = list(map(int, right.strip().split(" ")))
                equations.append((result, operands))

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

    return equations


def dfs(target, operands, current):
    #print(f"[{target}] : {current} : {operands}")
    if current == target and len(operands) == 0:
        return True
    elif current > target or len(operands) == 0:
        return False

    op = operands.pop(0)
    concat_op = str(current) + str(op)
    return dfs(target, operands.copy(), current + op) or dfs(target, operands.copy(), current * op) or dfs(target, operands.copy(), int(concat_op))


def calibrate(equations):
    result = 0
    for equation in equations:
        target = equation[0]
        operands = equation[1]
        first_op = operands.pop(0)
        if dfs(target, operands, first_op):
            result += target
    return result


def main():
    filename = "input.txt"
    equations = read_input(filename)
    result = calibrate(equations)
    print(result)
    assert result == 661823605105500


if __name__ == "__main__":
    main()
