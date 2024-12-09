import re


def cleanup_donts(input_str):
    if input_str == '':
        return ""

    parts = input_str.split("don't()", 1)
    enabled_input = parts[0]
    addition = ""
    if len(parts) == 2:
        parts2 = parts[1].split("do()", 1)
        if len(parts2) == 2:
            addition = cleanup_donts(parts2[1])
    return enabled_input + addition


def process_input(file_content):
    result = 0

    cleaned_up_input = cleanup_donts(file_content)

    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    number_pattern = r"mul\((\d+),(\d+)\)"

    matches = re.findall(pattern, cleaned_up_input)
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
