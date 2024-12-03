import re


def parse_input():
    text = open("inputs/day3_input.txt").read().strip()
    # print(text[:10], text[-10:])
    return text


def solve_part1(text):
    pattern = re.compile(
        r"""
        mul         # match the literal 'mul'
        \(          # match the opening parenthesis
        \d{1,3}     # match 1 to 3 digits
        ,           # match the comma
        \d{1,3}     # match 1 to 3 digits
        \)          # match the closing parenthesis
        """,
        re.VERBOSE,
    )
    matches = re.findall(pattern, text)
    total = 0
    for match in matches:
        nums = match[4:-1].split(",")
        total += int(nums[0]) * int(nums[1])
    print(total)


if __name__ == "__main__":
    text = parse_input()
    solve_part1(text)
