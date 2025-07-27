from os import path
import sys
import numpy as np

def parse_levels(filename: str) -> list[list[int]]:
    """ Parse a text file with 5 columns (levels) per line as a list of reports"""
    reports = []
    with open(filename, "r") as f:
        for line in f:
            # Each level in the report is separate by a space
            res = line.strip().split(" ")
            reports.append([ int(x) for x in res ])

    return reports

if __name__ == "__main__":
    print("Starting")

    basepath = path.dirname(sys.argv[0])
    filename = path.join(basepath, "inputs.txt")
    # filename = path.join(basepath, "inputs_test.txt")
    reports = parse_levels(filename)

    # Part 1

    def safe_report_check(report: list[int]) -> bool:
        # Caculate the difference between adjacent levels in the report
        differences = np.ediff1d(report)

        # Check if all the differences increase or decrease
        all_increasing = np.all(differences >= 0)
        all_decreasing = np.all(differences <= 0)

        # All differences should be >= 1 and <= 3. Check this on the absolute value.
        abs_differences = np.abs(differences)
        all_diff_in_range = np.all(abs_differences >= 1) and np.all(abs_differences <= 3)

        # Condition for a safe report
        if (all_increasing or all_decreasing) and all_diff_in_range:
            return True
        return False

    # Iterate through the reports
    safe_count = 0
    for report in reports:
        if safe_report_check(report):
            safe_count += 1

    print("Safe reports: ", safe_count)

    # Part 2
    # Reimplementing part 1 but integrating the problem dampener

    safe_count = 0

    for report in reports:
        # Check the complete report
        if safe_report_check(report):
            safe_count += 1
        # If not safe, try to remove one element and re-check the report
        else:
            # Check with dampened_reports where one element has been removed from the original report
            for i in range(len(report)):
                dampened_report = report[0:i] + report[i+1:]
                if safe_report_check(dampened_report):
                    safe_count += 1
                    break


    print("Safe reports with dampener: ", safe_count)