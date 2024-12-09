def is_safe_report(levels):
    is_increasing = levels[0] < levels[1]
    
    for i in range(len(levels) - 1):
        if is_increasing:
            if levels[i] >= levels[i + 1] or abs(levels[i] - levels[i + 1]) > 3:
                return False
        else:
            if levels[i] <= levels[i + 1] or abs(levels[i] - levels[i + 1]) > 3:
                return False
    return True


def generate_sublists(lst):
    return [lst[:i] + lst[i+1:] for i in range(len(lst))]


def dampener(levels):
    sublists = generate_sublists(levels)
    for sublist in sublists:
        if is_safe_report(sublist):
            return True
    return False


def process_reports(filename):
    safe_reports = 0

    try:
        with open(filename, 'r') as file:
            for report in file:
                try:
                    levels = list(map(int, report.strip().split()))
                    if dampener(levels):
                        safe_reports += 1

                except ValueError:
                    print(f"Skipping line with invalid numbers: {report.strip()}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

    return safe_reports


def main():
    filename = "input.txt"
    safe_reports = process_reports(filename)
    print(safe_reports)


if __name__ == "__main__":
    main()
