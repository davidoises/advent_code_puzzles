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
    # filename = path.join(basepath, "inputs.txt")
    # filename = path.join(basepath, "inputs_test.txt")
    filename = path.join(basepath, "inputs_test_simple.txt")
    file = parse_file(filename)

    # Part 1

    def find_xmas_occurrences(file: list[str]) -> int:
        """ """

        occurrences = 0
        for line in file:
            line_ocurrences = line.count("XMAS") + line.count("SAMX")
            if line_ocurrences > 0:
                print(line, " : ", line_ocurrences)
            occurrences += line_ocurrences
        return occurrences

    print("Horizontal")
    # Find the XMAS in horizontal forward
    horizontal_occurrences = find_xmas_occurrences(file)

    print("Vertical")
    # Traspose the file to simplify seacrhing for ocurrences in vertical orientation
    verticalized_file = ["".join(s) for s in zip(*file)]
    # Find the XMAS in horizontal forward
    vertical_occurrences = find_xmas_occurrences(verticalized_file)

    print("Diagonal right")
    number_of_lines = len(file)
    number_of_cols = len(file[0])
    new_file_right = [ ["."]*number_of_cols for i in range(number_of_lines*number_of_cols)]
    diagonal_right_file = []


    # [file[0][0], file[1][1], file[2][2], file[3][3], file[4][4]]
    # [file[0][1], file[1][2], file[2][3], file[3][4], file[4][5]]
    # [file[0][2], file[1][3], file[2][4], file[3][5]]
    # [file[0][3]]

    # [file[1][0], file[2][1], file[3][2], file[4][3], file[5][4]]
    # [file[1][1], file[2][2], file[3][3], file[4][4], file[5][5]]
    # [file[1][1], file[2][2], file[3][3], file[4][4], file[5][5]]



    line_count = 0
    for i in range(number_of_lines):
        for j in range(number_of_cols):
            # print("Line")
            for z in range(number_of_cols):
                if (i+z) < number_of_lines and (j+z) < number_of_cols:
                    # print(f"[{i+z},{j+z}]")
                    new_file_right[line_count][z] = file[i+z][j+z]
            diagonal_right_file.append("".join(new_file_right[line_count]))
            line_count += 1

    horizontal_occurrences = find_xmas_occurrences(diagonal_right_file)



    