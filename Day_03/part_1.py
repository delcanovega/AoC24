import re


def process_input(file_content):
    result = 0

    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    number_pattern = r"mul\((\d+),(\d+)\)"

    matches = re.findall(pattern, file_content)
    for match in matches:
        operands = re.findall(number_pattern, match).pop()
        x = int(operands[0])
        y = int(operands[1])
        result += x * y

    return result


def read_input(filename):
    file_content = ""

    try:
        with open(filename, 'r') as file:
            file_content = file.read()

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

    return file_content


def main():
    filename = "input.txt"
    file_content = read_input(filename)
    result = process_input(file_content)
    print(result)


if __name__ == "__main__":
    main()
