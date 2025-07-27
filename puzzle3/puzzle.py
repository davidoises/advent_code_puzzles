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

    # Part 2

    # Apply a regular expression to get the expected format mul(x,y), do(), and don't().
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|do\(\)|don\'t\(\)", memory_contents)

    # Iterate through instructions and keep track if enabled or not
    enable_mul = True
    total_res = 0
    for instruction in matches:
        # Check if enable or disable the instructions
        if instruction == "do()":
            enable_mul = True
        elif instruction == "don't()":
            enable_mul = False
        else:
            if enable_mul:
                # If enabled, extract the multiplication arguments
                inner_match = re.match(r"mul\((\d{1,3}),(\d{1,3})\)", instruction)
                x = int(inner_match.group(1))
                y = int(inner_match.group(2))

                # Perform the multiplication
                res = x*y
                total_res += res
                
    print("total res: ", total_res)



