def part_1():
    """
    The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9
    This example data contains six reports each containing five levels.

    The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.
    In the example above, the reports can be found safe or unsafe by checking those rules:

    7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
    1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
    9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
    1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
    1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
    So, in this example, 2 reports are safe.

    Analyze the unusual data from the engineers. How many reports are safe?
    """
    safe_reports = 0
    all_reports = extract_reports_from_txt("day_2_inputs.txt")
    for report in all_reports:
        if safe_report(report):
            safe_reports += 1
    print(f"safe_reports: {safe_reports}")
    return safe_reports

def part_2():
    return

def extract_reports_from_txt(filepath):
    all_reports = []
    with open(filepath, "r") as file:
        for line in file:
            report = line.split()
            all_reports.append([int(x) for x in report])
    return all_reports

def safe_report(report):
    rising = 0
    falling = 0
    for i in range(len(report)-1):
        last_level = report[i]
        current_level = report[i+1]
        if levels_match(last_level, current_level):
            return False
        if step_size_unsafe(last_level, current_level):
            return False
        if level_rising(last_level, current_level):
            if falling > 0:
                return False
            rising += 1
        else:
            if rising > 0:
                return False
            falling += 1
    return True
        

def levels_match(last_level, current_level):
    return last_level == current_level

def level_rising(last_level, current_level):
    return current_level > last_level

def step_size_unsafe(last_level, current_level):
    if abs(current_level - last_level) > 3:
        return True
    return False

if __name__ == "__main__":
    part_1()
    part_2()