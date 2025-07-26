import numpy as np

def parse_schematics_files(filename: str) -> (list[list[int]], list[list[int]]):
    
    # Resulting lists start empty.
    # Each list's element contains an array describing the spaces taken by the lock or key.
    # Example: Locks[0] = [0, 5, 4, 2, 2]
    locks = []
    keys = []
    
    with open(filename, "r") as f:
        
        # Indicates we are trying to find the start of a new lock/key
        new_part = True
        is_lock = True

        # Number of spaces used by the current lock/key
        colum_lengths = [0, 0, 0, 0, 0]

        # Count of lines processed of the current object schematic
        line_count = 0

        for line in f:
            # Detecting the start of a new lock or key
            if new_part:
                if "#####" in line:
                    new_part = False
                    # print("Start")
                    is_lock = True
                elif "....." in line:
                    new_part = False
                    # print("Start")
                    is_lock = False
                else:
                    pass

                # Continue so we ignore this line
                continue

            # Count the spaces used by the lock or key per column
            line_count += 1
            for i in range(5):
                if line[i] == "#" and line_count <= 5:
                    colum_lengths[i] += 1

            # Detecting the end the lock or key
            if line_count == 6:
                # print("end")
                if is_lock:
                    locks.append(colum_lengths)
                else:
                    keys.append(colum_lengths)

                # Rreset parsing states
                new_part = True
                colum_lengths = [0, 0, 0, 0, 0]
                line_count = 0
    
    return (locks, keys)

if __name__ == "__main__":
    print("Starting")

    locks, keys = parse_schematics_files("inputs_25.txt")

    print("Processed ", len(locks), " locks schematics")
    print("Processed ", len(keys), " keys schematics")

    # Keep track of matches between keys and locks
    match_count = 0

    for lock in locks:
        for key in keys:

            # Add the lock/key pair
            addition = np.add(lock, key)

            # Check if there are overlaps in the combination
            overlaps = addition > 5
            fits = not np.any(overlaps)

            # Increase the match count
            if fits:
                match_count += 1

    print("Matches: ", match_count)