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
    """
    The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

    The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

    Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

    More of the above example's reports are now safe:

    7 6 4 2 1: Safe without removing any level.
    1 2 7 8 9: Unsafe regardless of which level is removed.
    9 7 6 2 1: Unsafe regardless of which level is removed.
    1 3 2 4 5: Safe by removing the second level, 3.
    8 6 4 4 1: Safe by removing the third level, 4.
    1 3 6 7 9: Safe without removing any level.
    Thanks to the Problem Dampener, 4 reports are actually safe!

    Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
    """
    part_2_safe_reports = 0
    all_reports = extract_reports_from_txt("day_2_inputs.txt")

    for report in all_reports:
        clean_report = clean_up(report)
        report_check = safe_report(clean_report)
        if report_check == []:
            part_2_safe_reports += 1 
        else:
            pass
            # print(f"report: {report}, clean_report: {clean_report}, report_check: {report_check}")
    print(f"part_2_safe_reports: {part_2_safe_reports}")
    return part_2_safe_reports


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

    errors = []
    for i in range(len(report) - 1):
        last_level = report[i]
        current_level = report[i + 1]

        if levels_match(last_level, current_level):
            errors.append(f"levels_match")
        if step_size_unsafe(last_level, current_level):
            errors.append(f"step_size_unsafe")
        if level_rising(last_level, current_level):
            rising += 1
        else:
            falling += 1

        if rising == 1 and falling == 1:
            errors.append("fall_rise")

    return errors


def clean_up(report):
    report_len = len(report)
    first_index_in_report = 0
    last_index_in_report = report_len - 1
    penultimate_index = report_len - 2
    one_before_penultimate_index = report_len - 3
    for i in range(last_index_in_report):
        level_1 = report[i]
        level_2 = report[i + 1]
    
        # check if levels rise and fall
        if i <= one_before_penultimate_index:
            level_3 = report[i + 2]
            if do_levels_rise_and_fall(level_1, level_2, level_3):
                del report[i + 1]
                break

        if levels_match(level_1, level_2):
            del report[i]
            break

        if step_size_unsafe(level_1, level_2):
            if i == first_index_in_report:
                del report[first_index_in_report]
            if i == penultimate_index:
                del report[last_index_in_report]
            break

    return report

def do_levels_rise_and_fall(level_1, level_2, level_3):
    if level_1 >= level_2 >= level_3:
        return False
    if level_1 <= level_2 <= level_3:
        return False
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
