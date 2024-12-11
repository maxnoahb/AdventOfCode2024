import numpy as np


def parse_input():
    """Split input file into a list of lists of integers."""
    lines = open("inputs/day2.txt").read().strip().splitlines()
    lines = [line.split() for line in lines]
    return lines


def check_line(line):
    """
    Check if a list of numbers meets the criteria: all numbers are in ascending or descending order,
    and the difference between each number is between 1 and 3.

    Parameters:
    line (list): A list of integers representing a line.

    Returns:
    bool: True if the line meets the criteria, False otherwise.
    """
    line = [int(num) for num in line]
    sorted_asc = sorted(line)
    sorted_desc = sorted(line, reverse=True)
    diffs = np.diff(line)
    disqualifying_diffs = list(filter(lambda x: abs(x) == 0 or abs(x) > 3, diffs))

    if not disqualifying_diffs and (line == sorted_asc or line == sorted_desc):
        return True
    return False


def solve_part1(lines):
    """
    Counts the number of lines that pass the check_line function.

    Args:
        lines (list): A list of strings representing lines of input.

    Returns:
        None
    """
    total = 0
    for line in lines:
        if check_line(line):
            total += 1
    print(total)


def solve_part2(lines):
    """
    Counts the number of valid lines in the given list of lines.
    A line is considered valid if it passes the check_line function.
    If a line is not valid, it checks if removing any single character from the line makes it valid.
    Returns the total count of valid lines.

    Args:
        lines (list): A list of strings representing lines.

    Returns:
        int: The total count of valid lines.
    """
    total = 0
    for line in lines:
        if check_line(line):
            total += 1
        else:
            for i in range(len(line)):
                line_copy = line.copy()
                line_copy.pop(i)
                if check_line(line_copy):
                    total += 1
                    break
    print(total)


if __name__ == "__main__":
    lines = parse_input()
    solve_part1(lines)
    solve_part2(lines)
