from os import path
import sys
import re

def parse_memory(filename: str) -> str:
    """ Read all inputs as a single string"""

    contents = ""
    with open(filename, "r") as f:
        contents = f.read()
    return contents

if __name__ == "__main__":
    print("Starting")

    basepath = path.dirname(sys.argv[0])
    filename = path.join(basepath, "inputs.txt")
    # filename = path.join(basepath, "inputs_test.txt")
    memory_contents = parse_memory(filename)

    # Part 1

    # Apply a regular expression to get the expected format mul(x,y).
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", memory_contents)

    total_res = 0
    for x,y in matches:
        res = int(x)*int(y)
        total_res += res
        # print(f"Found: mul({x},{y}) = {res}")
    print("total res: ", total_res)

