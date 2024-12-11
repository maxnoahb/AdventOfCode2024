import re


def parse_input():
    text = open("inputs/day3.txt").read().strip()
    return text


def solve_part1(text):
    """
    Calculates the total by multiplying pairs of numbers enclosed in 'mul' parentheses.

    Args:
        text (str): The input text containing the 'mul' expressions.

    Returns:
        None: The function prints the total.

    Example:
        >>> solve_part1("mul(2,3)catsmul(4 5)catsmul(6,7)")
        68
    """
    pattern = re.compile(
        r"""
        mul         # match the literal 'mul'
        \(          # match the opening parenthesis
        (\d{1,3})   # match 1 to 3 digits (capture group)
        ,           # match the comma
        (\d{1,3})   # match 1 to 3 digits (capture group)
        \)          # match the closing parenthesis
        """,
        re.VERBOSE,
    )
    matches = re.findall(pattern, text)
    total = 0
    for a, b in matches:
        total += int(a) * int(b)
    print(total)


def solve_part2(text):
    """
    Calculates the total by multiplying pairs of numbers based on the given text.

    Args:
        text (str): The input text containing commands and numbers.

    Returns:
        None: This function does not return anything. It prints the total.

    Example:
        >>> solve_part2("mul(2,3) do() mul(4,5) don't() mul(6,7)")
        26
    """
    pattern = re.compile(
        r"""
        mul         # match the literal 'mul'
        \(          # match the opening parenthesis
        (\d{1,3})   # match 1 to 3 digits (capture group)
        ,           # match the comma
        (\d{1,3})   # match 1 to 3 digits (capture group)
        \)          # match the closing parenthesis
        |           # or
        do\(\)      # match the literal 'do()'
        |           # or
        don't\(\)   # match the literal 'don't()'
        """,
        re.VERBOSE,
    )
    matches = re.finditer(pattern, text)
    total = 0
    do = True
    for match in matches:
        command, a, b = match.group(0, 1, 2)
        if command == "do()":
            do = True
        elif command == "don't()":
            do = False
        elif do:
            total += int(a) * int(b)
        else:
            pass
    print(total)


if __name__ == "__main__":
    text = parse_input()
    solve_part1(text)
    solve_part2(text)
