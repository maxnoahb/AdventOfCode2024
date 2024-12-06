from helpers import parse_grid_file

DIAGONAL_OFFSETS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
ALL_OFFSETS = DIAGONAL_OFFSETS + [(0, 1), (0, -1), (-1, 0), (1, 0)]


def parse_input():
    """
    Parses the input file and returns a dictionary of coordinates and characters.
    e.g. {(0, 0): "X", (0, 1): "A", ...}

    Returns:
        dict: A dictionary where the keys are coordinates (tuples of integers) and the values are characters.
    """
    return parse_grid_file("inputs/day4_input.txt")


def find_sequence(coords, sequence, offset):
    """
    Check if a given sequence of characters matches the characters in
    the dictionary at the specified coordinates.

    Args:
        coords (tuple): The starting coordinates to check the sequence from.
        sequence (str): The sequence of characters to check.
        offset (tuple): The offset to increment the coordinates for each character in the sequence.

    Returns:
        bool: True if the sequence matches the characters in the dictionary at the specified coordinates, False otherwise.
    """
    for i, char in enumerate(sequence):
        new_coords = (coords[0] + ((i + 1) * offset[0]), coords[1] + ((i + 1) * offset[1]))
        if coords_dict.get(new_coords) != char:
            return False
    return True


def solve_part1(coords_dict):
    """
    Counts the number of occurrences of an "XMAS" sequence in the coordinates dictionary.
    The sequence can be in any direction (horizontal, vertical, diagonal).
    """
    total = 0
    for coords, val in list(coords_dict.items()):
        if val == "X":
            for offset in ALL_OFFSETS:
                if find_sequence(coords, "MAS", offset):
                    total += 1
    print(total)


def solve_part2(coords_dict):
    """
    Finds the number of X-shaped patterns of "MAS" in the given dictionary of coordinates.
    E.g.
        M . S
        . A .
        S . M
    The MAS patterns can go in any direction but must cross each other diagonally.

    Args:
        coords_dict (dict): A dictionary containing coordinates as keys and values representing characters.

    Returns:
        None
    """
    total = 0
    for coords, val in list(coords_dict.items()):
        # we will check for an A, so that we can begin from the center of the X
        if val == "A":
            # check for an M and S in opposite diagonal directions
            for offset in DIAGONAL_OFFSETS:
                if find_sequence(coords, "M", offset):
                    opp_offset = (-offset[0], -offset[1])
                    if find_sequence(coords, "S", opp_offset):
                        remaining_offsets = [
                            o for o in DIAGONAL_OFFSETS if o not in (offset, opp_offset)
                        ]
                        # check for another M and S in the remaining diagonal directions
                        for offset2 in remaining_offsets:
                            if find_sequence(coords, "M", offset2):
                                opp_offset2 = (-offset2[0], -offset2[1])
                                if find_sequence(coords, "S", opp_offset2):
                                    total += 1
                    break
    print(total)


if __name__ == "__main__":
    coords_dict = parse_input()
    solve_part1(coords_dict)
    solve_part2(coords_dict)
