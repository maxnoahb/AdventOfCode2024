def parse_grid_file(file):
    """
    Parses the input file and returns a dictionary of coordinates and characters.
    e.g. {(0, 0): "X", (0, 1): "A", ...}

    Returns:
        dict: A dictionary where the keys are coordinates (tuples of integers) and the values are characters.
    """
    lines = open(file).read().strip().splitlines()
    coords_dict = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            coords_dict[(i, j)] = char
    return coords_dict
