import re
from operator import xor


COMPUTER = {
    "A": 0,
    "B": 0,
    "C": 0,
    "P": 0,
}
OUTPUT_QUEUE = []


def read_input(filename):
    program = []
    try:
        with open(filename, 'r') as file:
            regex = r"(\d+)\s*\n|(\d{1,3}(?:,\d{1,3})*)"
            matches = re.findall(regex, file.read())
            matches = [match[0] if match[0] else match[1] for match in matches]
            COMPUTER["A"] = int(matches[0])
            COMPUTER["B"] = int(matches[1])
            COMPUTER["C"] = int(matches[2])
            program = list(map(int, matches[3].split(",")))
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

    return program


def combo(operand):
    if operand < 4:
        return operand
    elif operand == 4:
        return COMPUTER["A"]
    elif operand == 5:
        return COMPUTER["B"]
    elif operand == 6:
        return COMPUTER["C"]
    else:
        raise ValueError("This should not happen")


def adv(operand):
    COMPUTER["A"] //=  pow(2, combo(operand))


def bxl(operand):
    COMPUTER["B"] = xor(COMPUTER["B"], operand)


def bst(operand):
    COMPUTER["B"] = combo(operand) % 8


def jnz(operand):
    if COMPUTER["A"] == 0:
        return
    COMPUTER["P"] = operand - 2 if COMPUTER["P"] != operand else operand


def bxc(_):
    COMPUTER["B"] = xor(COMPUTER["B"], COMPUTER["C"])


def out(operand):
    OUTPUT_QUEUE.append(str(combo(operand) % 8))


def bdv(operand):
    COMPUTER["B"] = COMPUTER["A"] // pow(2, combo(operand))


def cdv(operand):
    COMPUTER["C"] = COMPUTER["A"] // pow(2, combo(operand))


OPERATIONS = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv,
}


def execute(program):
    while COMPUTER["P"] < len(program):
        opcode = program[COMPUTER["P"]]
        OPERATIONS[opcode](program[COMPUTER["P"] + 1])
        COMPUTER["P"] += 2


def main():
    filename = "input.txt"
    program = read_input(filename)
    execute(program)
    result = ",".join(OUTPUT_QUEUE)
    print(result)
    assert result == "4,6,1,4,2,1,3,1,6"


if __name__ == "__main__":
    main()
