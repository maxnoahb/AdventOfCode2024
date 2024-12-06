from itertools import cycle

from helpers import parse_grid_file


def parse_input():
    return parse_grid_file("inputs/day6_input.txt")


def solve_part1(grid):
    # start going straight up, and the next item in the list is always a right turn
    dirs = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])
    next_dir = next(dirs)
    start = next(coords for coords, char in grid.items() if char == "^")
    visited = set([start])

    while True:
        row, col = start
        next_coords = (row + next_dir[0], col + next_dir[1])
        if next_coords not in grid:
            break
        if grid[next_coords] == "#":
            next_dir = next(dirs)
        else:
            visited.add(next_coords)
            start = next_coords

    print(len(visited))


if __name__ == "__main__":
    grid = parse_input()
    solve_part1(grid)
