from collections import Counter


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


def prepare_occurrences(second_list):
    return dict(Counter(second_list))


def calculate_similarity(first_list, occurrences):
    first_list.sort()

    acc_similarity = 0
    for num in first_list:
        acc_similarity += num * occurrences.get(num, 0)

    return acc_similarity


def main():
    filename = "input.txt"
    first_list, second_list = read_numbers_from_file(filename)
    occurrences = prepare_occurrences(second_list)
    acc_distances = calculate_similarity(first_list, occurrences)
    print(acc_distances)


if __name__ == "__main__":
    main()
