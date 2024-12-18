def read_input(filename):
    files = []
    spaces = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                i = 0
                for block in line.strip():
                    block = int(block)
                    if i % 2 == 0:
                        files.append(block)
                    else:
                        spaces.append(block)
                    i += 1

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

    return files, spaces


def calculate_checksum(memory):
    checksum = 0
    i = 0
    while memory[i] != ".":
        checksum += i * int(memory[i])
        i += 1
    return checksum


def compact(memory):
    i = 0
    j = len(memory) - 1
    while memory[i] != ".":
        i += 1
    while memory[j] == ".":
        j -= 1

    while j > i:
        memory[i] = memory[j]
        memory[j] = "."
        while memory[i] != ".":
            i += 1
        while memory[j] == ".":
            j -= 1
    return memory


def paint_memory(files, spaces):
    memory = []
    for i in range(len(spaces)):
        for j in range(files[i]):
            memory.append(str(i))
        for j in range(spaces[i]):
            memory.append(".")
    for j in range(files[-1]):
        memory.append(str(len(files) - 1))
    return compact(memory)


def main():
    filename = "input.txt"
    files, spaces = read_input(filename)
    memory = paint_memory(files, spaces)
    result = calculate_checksum(memory)
    print(result)
    assert result == 6471961544878


if __name__ == "__main__":
    main()
