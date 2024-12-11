from itertools import product
from functools import lru_cache


def parse_input():
    """
    Parses the input file and returns two lists: answers_list and operands_list.

    Returns:
        answers_list (list): A list of integers representing the answers to target.
        operands_list (list): A list of lists, where each inner list contains integers representing operands.
    """
    lines = open("inputs/day7.txt").read().strip().splitlines()
    answers_list = []
    operands_list = []
    for line in lines:
        k, v = line.split(": ")
        answers_list.append(int(k))
        operands_list.append(list(map(int, v.split(" "))))
    return answers_list, operands_list


def evaluate_expression(operands, operators, target):
    """
    Evaluate the expression represented by operands and operators, from left to right
    instead of following the order of operations.

    Args:
        operands (list): A list of operands.
        operators (list): A list of operators.
        target (int): The target value.

    Returns:
        int or None: The result of the evaluated expression, or None if the result exceeds the target value.
    """
    result = operands[0]
    for i, op in enumerate(operators):
        if op == "+":
            result += operands[i + 1]
        elif op == "*":
            result *= operands[i + 1]
        elif op == "||":
            result = int(f"{result}{operands[i + 1]}")
        if result > target:
            return None
    return result


@lru_cache(None)
def eval_all_possibilities(operators, answer, operands):
    """
    Check all operator combinations to see if any match the target answer.
    Calculate the Cartesian product of the operators list with itself to find
    all possible permutations of the operators.

    Parameters:
    - operators (list): A list of operators to be used in the expression.
    - answer (int): The target answer to match.
    - operands (list): A list of operands to be used in the expression.

    Returns:
    - int or None: The target answer if a matching combination is found, None otherwise.
    """
    # Ensure inputs are hashable
    operators_tuple = tuple(operators)
    operands_tuple = tuple(operands)

    for op_comb in product(operators_tuple, repeat=len(operands_tuple) - 1):
        result = evaluate_expression(operands_tuple, op_comb, answer)
        if result == answer:
            return answer
    return None


def solve(answers_list, operands_list, operators):
    """
    This function calculates the total by evaluating all possibilities of applying the given operators
    to the corresponding operands and checking if they match the answer. The total is printed at the end.

    Parameters:
    - answers_list (list): A list of answers.
    - operands_list (list): A list of operands.
    - operators (list): A list of operators.

    Returns:
    - None
    """
    total = 0
    # convert operators to a tuple so it can be used as a key in the lru_cache
    operators_tuple = tuple(operators)
    for answer, operands in zip(answers_list, operands_list):
        operands_tuple = tuple(operands)
        if matched_answer := eval_all_possibilities(operators_tuple, answer, operands_tuple):
            total += matched_answer
    print(total)


if __name__ == "__main__":
    answers_list, operands_list = parse_input()
    solve(answers_list, operands_list, ["+", "*"])
    solve(answers_list, operands_list, ["+", "*", "||"])
