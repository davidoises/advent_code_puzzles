
import numpy as np

def parse_lists(filename: str) -> tuple[list[int],list[int]]:
    """ Parse a text file with 2 columns and return a left list and a right list of ints """
    
    # Resulting lists start empty
    left_list = []
    right_list = []

    with open(filename, "r") as f:
        for line in f:
            # Process each line and separate columns, add elements to either left or right list.
            res = line.strip().split("   ")
            left_list.append(int(res[0]))
            right_list.append(int(res[1]))

    return left_list, right_list

if __name__ == "__main__":
    print("Starting")

    left_list, right_list = parse_lists("inputs_1.txt")
    # left_list, right_list = parse_lists("inputs_1_test.txt")

    # Part 1

    # Sort both lists.
    left_list.sort()
    right_list.sort()

    # Since both lists are already sorted we can directly use np.subtract with absolute value
    distances = np.abs(np.subtract(right_list, left_list))

    # Aggregate all into a total distance value
    total_distance = distances.sum()
    print("total distance: ", total_distance)

    # Part 2

    # Count repetitions of values in the right list
    unique, counts = np.unique(right_list, return_counts=True)
    # Create a dictionary where they key is the Id and the value is the repetition count
    occurrences = dict(zip(unique, counts))

    similarity_list = []
    for x in left_list:
        
        # Try to get the number of repetitions from the current element of the left list in the right list.
        frequency = 0
        if x in occurrences.keys():
            frequency = occurrences[x]

        # Its score is the value * frequency
        similarity_list.append(x * frequency)

    # Aggregate all scores into a total score
    similarity_score = np.sum(similarity_list)
    print("similarity score: ", similarity_score)