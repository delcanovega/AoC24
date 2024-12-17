from math import floor


def is_valid_update(requirements_by_page, update):
    printed_pages = set([])
    for page in update:
        required_pages = set(requirements_by_page.get(page, []))
        active_requirements = required_pages.intersection(set(update))
        if not active_requirements.issubset(printed_pages):
            return False
        printed_pages.add(page)
    return True


def calculate(requirements_by_page, updates):
    result = 0
    for update in updates:
        if is_valid_update(requirements_by_page, update):
            result += update[floor(len(update) / 2)]

    return result


def read_input(filename):
    requirements_by_page = {}
    updates = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                if "|" in line:
                    required_page, page = list(map(int, line.strip().split("|")))
                    requirements = requirements_by_page.get(page, [])
                    requirements.append(required_page)
                    requirements_by_page[page] = requirements
                elif line != "\n":
                    updates.append(list(map(int, line.strip().split(","))))

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

    return requirements_by_page, updates


def main():
    filename = "input.txt"
    requirements_by_page, updates = read_input(filename)
    result = calculate(requirements_by_page, updates)
    print(result)
    assert result == 6242


if __name__ == "__main__":
    main()
