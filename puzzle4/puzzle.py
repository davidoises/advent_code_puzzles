from os import path
import sys
import re

def parse_file(filename: str) -> list[str]:
    """ """

    file = []
    with open(filename, "r") as f:
        for line in f:
            file.append(line.strip())
    return file

if __name__ == "__main__":
    print("Starting")

    basepath = path.dirname(sys.argv[0])
    filename = path.join(basepath, "inputs.txt")
    # filename = path.join(basepath, "inputs_test.txt")
    # filename = path.join(basepath, "inputs_test2.txt")
    # filename = path.join(basepath, "inputs_test_simple.txt")
    file = parse_file(filename)

    # Part 1

    def find_xmas_occurrences(file: list[str]) -> int:
        """ Check the occurrences of XMAS in forwards and backwards direction """

        occurrences = 0
        for line in file:
            line_ocurrences = line.count("XMAS") + line.count("SAMX")
            occurrences += line_ocurrences
        return occurrences
    
    # Traspose the file to simplify seacrhing for ocurrences in vertical orientation
    verticalized_file = ["".join(s) for s in zip(*file)]
    
    # Generate new files with the lines formed by top to down left and right diagonals
    number_of_lines = len(file)
    number_of_cols = len(file[0])
    diagonal_right_file = []
    diagonal_left_file = []

    # ↙ Top to bottom left
    # All the diagonals in this direction follow the behavior of row index + col index = a fixed distance
    # The first D is the top left corner, d = 0 + 0 = 0
    for d in range(number_of_lines + number_of_cols - 1):
        line = []
        for r in range(number_of_lines):
            c = d - r
            if 0 <= c < number_of_cols:
                line.append(file[r][c])
        if line:
            diagonal_left_file.append(''.join(line))


    # ↘ Top to bottom right
    # All the diagonals in this direction follow the behavior of row index - col index = a fixed distance
    # The first D is the top right corner, d = 0 - 5 = -5 (assuming 5 cols)
    for d in range(-number_of_cols + 1, number_of_lines):
        line = []
        for r in range(number_of_lines):
            c = r - d
            if 0 <= c < number_of_cols:
                line.append(file[r][c])
        if line:
            diagonal_right_file.append(''.join(line))

    # Find all occurrences
    horizontal_occurrences = find_xmas_occurrences(file)
    vertical_occurrences = find_xmas_occurrences(verticalized_file)
    diagonal_right_occurrences = find_xmas_occurrences(diagonal_right_file)
    diagonal_left_occurrences = find_xmas_occurrences(diagonal_left_file)
    total_occurrences = horizontal_occurrences + vertical_occurrences + diagonal_right_occurrences + diagonal_left_occurrences
    print("total occurrences of XMAS: ", total_occurrences)

    # Part 2

    characters = []
    for line in file:
        characters.append(list(line))
    
    match_count = 0
    rows = len(characters)
    cols = len(characters[0])
    # Iterate through rows skiping borders
    for r in range(1, rows-1):
        # Iterate through cols skiping borders
        for c in range(1, cols-1):

            # Found a possible center of a X
            if characters[r][c] == "A":
                match = True
                # test posibilities for ↘ diagonal
                above_left = characters[r-1][c-1]
                down_right = characters[r+1][c+1]
                match &= (above_left == "M" and down_right == "S") or (above_left == "S" and down_right == "M")

                # test posibilities for ↙ diagonal
                above_right = characters[r-1][c+1]
                down_left = characters[r+1][c-1]
                match &= (above_right == "M" and down_left == "S") or (above_right == "S" and down_left == "M")

                if match:
                    match_count += 1

    print("total occurrences of X-MAS: ", match_count)
