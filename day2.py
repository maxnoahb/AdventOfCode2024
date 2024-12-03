import numpy as np


def parse_input():
    lines = open("inputs/day2_input.txt").read().strip().splitlines()
    lines = [line.split() for line in lines]
    # print(lines[:2])
    return lines


def check_line(line):
    line = [int(num) for num in line]
    sorted_asc = sorted(line)
    sorted_desc = sorted(line, reverse=True)
    diffs = np.diff(line)
    disqualifying_diffs = list(filter(lambda x: abs(x) == 0 or abs(x) > 3, diffs))
    # print(sorted_asc, sorted_desc, disqualifying_diffs)
    if not disqualifying_diffs and (line == sorted_asc or line == sorted_desc):
        return True
    return False


def solve_part1():
    lines = parse_input()
    total = 0
    for line in lines:
        if check_line(line):
            total += 1
    print(total)


if __name__ == "__main__":
    solve_part1()
