def read_numbers_from_file(filename):
    first_list = []
    second_list = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split()

                if len(parts) != 2:
                    print(f"Skipping invalid line: {line.strip()}")
                    continue

                try:
                    first_num = int(parts[0])
                    second_num = int(parts[1])

                    first_list.append(first_num)
                    second_list.append(second_num)
                except ValueError:
                    print(f"Skipping line with invalid numbers: {line.strip()}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

    return first_list, second_list


def calculate_distances(first_list, second_list):
    first_list.sort()
    second_list.sort()

    acc_distances = 0
    for left, right in zip(first_list, second_list):
        acc_distances += abs(left - right)

    return acc_distances


def main():
    filename = "input.txt"
    first_numbers, second_numbers = read_numbers_from_file(filename)
    acc_distances = calculate_distances(first_numbers, second_numbers)
    print(acc_distances)


if __name__ == "__main__":
    main()
