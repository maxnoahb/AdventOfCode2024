OFFSETS = [(0, 1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)]


def parse_input():
    lines = open("inputs/day4_input.txt").read().strip().splitlines()
    coords_dict = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            coords_dict[(i, j)] = char
    # print(coords_dict)
    return coords_dict


def find_sequence(coords, sequence, offset):
    for i, char in enumerate(sequence):
        new_coords = (coords[0] + ((i + 1) * offset[0]), coords[1] + ((i + 1) * offset[1]))
        # print(new_coords, coords_dict.get(new_coords))
        if coords_dict.get(new_coords) != char:
            return False
        # print(f"{char}: ", new_coords)
    return True


def solve_part1(coords_dict):
    total = 0
    for coords, val in list(coords_dict.items()):
        if val == "X":
            # print("X: ", coords)
            for offset in OFFSETS:
                if find_sequence(coords, "MAS", offset):
                    total += 1
    print(total)


if __name__ == "__main__":
    coords_dict = parse_input()
    solve_part1(coords_dict)
