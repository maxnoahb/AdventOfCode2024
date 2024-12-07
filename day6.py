from itertools import cycle

from helpers import parse_grid_file

# directions for navigation: up, right, down, left (start from up, next in list is always a right turn)
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def parse_input():
    """Parse the input file into a grid representation."""
    return parse_grid_file("inputs/day6_input.txt")


def find_start_position(grid, start_char="^"):
    """Find the starting position of the given character in the grid."""
    return next(coords for coords, char in grid.items() if char == start_char)


def move_in_direction(position, direction):
    """Calculate the next position given the current position and direction."""
    row, col = position
    dr, dc = direction
    return row + dr, col + dc


def solve_part1(grid):
    """
    Find the number of visited positions in the grid, turning right when hitting an obstacle.
    Finish when exiting the grid.

    Args:
        grid (dict): A dictionary representing the grid.

    Returns:
        set: A set of visited positions.

    """
    direction_cycle = cycle(DIRECTIONS)
    curr_dir = next(direction_cycle)
    curr_pos = find_start_position(grid)
    visited = set([curr_pos])

    while True:
        next_pos = move_in_direction(curr_pos, curr_dir)
        # stop if out of bounds
        if next_pos not in grid:
            break
        # if we hit an obstacle, turn right
        if grid[next_pos] == "#":
            curr_dir = next(direction_cycle)
        else:
            visited.add(next_pos)
            curr_pos = next_pos

    print(len(visited))
    return visited


def solve_part2(grid, visited):
    """
    This function takes a grid and a set of visited cells as input. It loops through the visited cells
    and checks if adding an obstacle will create a cycle. It keeps track of the total number of cycles
    found and prints the result.

    Args:
        grid (dict): A dictionary representing the grid with cell coordinates as keys and cell values as values.
        visited (set): A set of cell coordinates that were visited in part 1.

    Returns:
        None
    """

    total_cycles = 0
    # we only need to consider the cells that were visited in part 1
    grid_visited = {coords: char for coords, char in grid.items() if coords in visited}

    # loop through the visited cells to check if adding an obstacle will create a cycle
    for pos, char in grid_visited.items():
        if char in ("^", "#"):
            continue

        # add an obstacle
        grid[pos] = "#"
        direction_cycle = cycle(DIRECTIONS)
        curr_dir = next(direction_cycle)
        curr_pos = find_start_position(grid)

        # keep track of visited cells with the direction included
        # this is to check if we've visited the same cell with the same direction before
        visited = set([curr_pos + curr_dir])

        while True:
            next_pos = move_in_direction(curr_pos, curr_dir)
            if next_pos not in grid:
                break
            if grid[next_pos] == "#":
                # check for a cycle
                if (coords_plus_dir := next_pos + curr_dir) in visited:
                    total_cycles += 1
                    break
                else:
                    visited.add(coords_plus_dir)
                    curr_dir = next(direction_cycle)
            else:
                visited.add(next_pos + curr_dir)
                curr_pos = next_pos

        grid[pos] = "."

    print(total_cycles)


if __name__ == "__main__":
    grid = parse_input()
    visited = solve_part1(grid)
    solve_part2(grid, visited)
