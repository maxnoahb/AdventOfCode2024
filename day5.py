def parse_input():
    """
    Parses the input file and returns the rules and updates.

    Returns:
        tuple: A tuple containing two lists. The first list contains the rules,
               where each rule is represented as a tuple of two integers. The second
               list contains the updates, where each update is represented as a list
               of integers.
    """
    lines = open("inputs/day5.txt").read().strip().splitlines()
    split_index = lines.index("")
    rules, updates = lines[:split_index], lines[split_index + 1 :]
    rules = [(int(a), int(b)) for a, b in [rule.split("|") for rule in rules]]
    updates = [[int(x) for x in update] for update in [u.split(",") for u in updates]]
    return rules, updates


def passes_rule(update, rule):
    """
    Checks if a given update passes a rule. An update passes a rule if the left
    integer appears before the right integer in the update.

    Args:
        update (list): The update to be checked.
        rule (tuple): The rule to be applied.

    Returns:
        bool: True if the update passes the rule, False otherwise.
    """
    left, right = rule
    # if the left or right integer is not in the update, the rule is satisfied
    if left not in update or right not in update:
        return True
    left_index, right_index = update.index(left), update.index(right)
    return left_index < right_index


def solve_part1(rules, updates):
    """
    Calculates the total sum of middle numbers in the updates list that pass all the given rules.

    Args:
        rules (list): A list of rules to check against the updates.
        updates (list): A list of updates to check against the rules.

    Returns:
        None: The function prints the total sum of middle numbers that pass all the rules.
    """
    total = 0
    for update in updates:
        if all([passes_rule(update, rule) for rule in rules]):
            middle_number = update[len(update) // 2]
            total += middle_number
    print(total)


def solve_part2(rules, updates):
    """
    Calculates the total sum of middle numbers in the updates list that DON'T pass all the given rules,
    after swapping the integers in the updates list to satisfy the rules.

    Args:
        rules (list): A list of rules.
        updates (list): A list of updates.

    Returns:
        None
    """
    total = 0
    for update in updates:
        # check for unsatisfied rules
        if not all([passes_rule(update, rule) for rule in rules]):
            # loop through the update list and swap the integers to satisfy the rules
            for i in range(len(update)):
                for j in range(i):
                    # if there is an existing rule that is not satisfied, swap the integers
                    if (update[j], update[i]) in rules:
                        update[j], update[i] = update[i], update[j]
            middle_number = update[len(update) // 2]
            total += middle_number
    print(total)


if __name__ == "__main__":
    rules, updates = parse_input()
    solve_part1(rules, updates)
    solve_part2(rules, updates)
