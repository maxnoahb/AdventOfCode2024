from collections import Counter


def parse_input():
    """
    Parses the input file and returns two sorted lists.

    Returns:
        list: The first sorted list.
        list: The second sorted list.
    """
    lines = open("inputs/day1_input.txt").read().strip().splitlines()
    list1, list2 = [], []
    for line in lines:
        num_list = line.split()
        list1.append(int(num_list[0]))
        list2.append(int(num_list[1]))
    list1.sort()
    list2.sort()
    return list1, list2


def solve_part1(list1, list2):
    """
    Calculates the total sum of absolute differences between corresponding elements of two lists.

    Args:
        list1 (list): The first list of numbers.
        list2 (list): The second list of numbers.

    Returns:
        None: This function does not return a value. It prints the total sum of absolute differences.
    """
    tuple_list = list(zip(list1, list2))
    diff_list = [abs(a - b) for a, b in tuple_list]
    total = sum(diff_list)
    print(total)


from collections import Counter


def solve_part2(list1, list2):
    """
    Calculates the total sum of the products of each number in list1 with its corresponding count in list2.

    Args:
        list1 (list): The first list of numbers.
        list2 (list): The second list of numbers.

    Returns:
        None: The function does not return a value. It prints the total sum of the products.

    Example:
        >>> list1 = [1, 2, 3]
        >>> list2 = [2, 2, 3, 3, 3]
        >>> solve_part2(list1, list2)
        23
    """
    total = 0
    count = Counter(list2)
    for num in list1:
        c = count[num]
        total += num * c
    print(total)


if __name__ == "__main__":
    list1, list2 = parse_input()
    solve_part1(list1, list2)
    solve_part2(list1, list2)
