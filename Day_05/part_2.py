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


def find_correct_order(requirements_by_page, update):
    blocked_pages = set()
    solution = []

    def dfs(current_page):
        print("Current page:", current_page, "- Blocked pages:", blocked_pages, " - solution:", solution)
        if current_page in solution or current_page in blocked_pages:
            return

        blocked_pages.add(current_page)

        dependencies = requirements_by_page.get(current_page, [])
        for dependency in dependencies:
            if dependency in update:
                dfs(dependency)

        blocked_pages.remove(current_page)
        solution.append(current_page)


    for page in update:
        if page not in solution:
            dfs(page)

    return solution


def calculate(requirements_by_page, updates):
    result = 0
    for update in filter(lambda u : not is_valid_update(requirements_by_page, u), updates):
        permutation = find_correct_order(requirements_by_page, update)
        print(update, "vs", permutation)
        result += 0 if permutation == [] else permutation[floor(len(permutation) / 2)]

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
    assert result == 5169


if __name__ == "__main__":
    main()
