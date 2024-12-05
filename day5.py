def parse_input():
    lines = open("inputs/day5_input.txt").read().strip().splitlines()
    split_index = lines.index("")
    rules, updates = lines[:split_index], lines[split_index + 1 :]
    rules = [(int(a), int(b)) for a, b in [rule.split("|") for rule in rules]]
    updates = [[int(x) for x in update] for update in [u.split(",") for u in updates]]
    return rules, updates


def passes_rule(update, rule):
    left, right = rule
    if left not in update or right not in update:
        return True
    left_index, right_index = update.index(left), update.index(right)
    return left_index < right_index


def solve_part1(rules, updates):
    print(rules[:5], updates[:5])
    total = 0
    for update in updates:
        if all([passes_rule(update, rule) for rule in rules]):
            middle_number = update[len(update) // 2]
            total += middle_number
    print(total)


if __name__ == "__main__":
    rules, updates = parse_input()
    solve_part1(rules, updates)
