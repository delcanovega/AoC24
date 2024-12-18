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
    while i < len(memory):
        if memory[i] != ".":
            checksum += i * int(memory[i])
        i += 1
    return checksum


def try_to_move_file(memory, file_id, file_size, file_idx, spaces_by_idx):
    for space_memory_idx, available_space in spaces_by_idx.items():
        if available_space >= file_size:
            write_idx = space_memory_idx
            while memory[write_idx] != "." and write_idx < len(memory) - 1:
                write_idx += 1
            if write_idx < file_idx:
                for k in range(file_idx, file_idx + file_size):
                    if memory[k] == str(file_id):
                        memory[k] = "."
                for _ in range(file_size):
                    memory[write_idx] = str(file_id)
                    write_idx += 1
                    available_space -= 1
                spaces_by_idx[space_memory_idx] = available_space
                #print("".join(memory))
                return


def compact(memory, files, spaces_by_idx, idx_by_file_id):
    file_id = len(files) - 1
    while file_id > 0:
        try_to_move_file(memory, file_id, files[file_id], idx_by_file_id[file_id], spaces_by_idx)
        file_id -= 1
    return memory


def paint_memory(files, spaces):
    memory = []
    idx_by_file_id = {}
    spaces_by_idx = {}
    for i in range(len(spaces)):
        idx_by_file_id[i] = len(memory)
        for j in range(files[i]):
            memory.append(str(i))
        spaces_by_idx[len(memory)] = spaces[i]
        for j in range(spaces[i]):
            memory.append(".")
    idx_by_file_id[len(files) - 1] = len(memory)
    for j in range(files[-1]):
        memory.append(str(len(files) - 1))
    return compact(memory, files, spaces_by_idx, idx_by_file_id)


def main():
    filename = "input.txt"
    files, spaces = read_input(filename)
    memory = paint_memory(files, spaces)
    result = calculate_checksum(memory)
    print(result)
    assert result == 6511178035564

if __name__ == "__main__":
    main()
