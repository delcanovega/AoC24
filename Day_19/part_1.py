
def read_input(filename):
    options = []
    designs = []
    try:
        with open(filename, 'r') as file:
            options = file.readline().strip().split(', ')
            file.readline()
            for line in file.readlines():
                designs.append(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

    return options, designs


def is_valid(design, options):
    fragment_set = set(options)

    dp = [False] * (len(design) + 1)
    dp[0] = True

    # Check each position in the target string
    for i in range(1, len(design) + 1):
        for j in range(i):
            if dp[j] and design[j:i] in fragment_set:
                dp[i] = True
                break

    return dp[len(design)]


def check_designs(options, designs):
    valid_designs = 0
    for design in designs:
        if is_valid(design, options):
            valid_designs += 1
    return valid_designs


def main():
    filename = "input.txt"
    options, designs = read_input(filename)
    result = check_designs(options, designs)
    print(result)
    assert result == 369


if __name__ == "__main__":
    main()
