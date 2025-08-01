#include <stdio.h> // printf
#include <fstream> // std::ifstream
#include <string> //std::string
#include <sstream> // std::istringstream
#include <algorithm> // std::sort
#include <cmath> // std::abs
#include <chrono> // std::chrono
#include <vector> // std::vectr
#include <tuple> // std::tuple
#include <unordered_map> // std::unordered_map

std::tuple<std::vector<int>, std::vector<int>> parse_lists(const std::string& file_name)
{
    std::vector<int> left_list;
    std::vector<int> right_list;

    std::ifstream input_file;
    input_file.open(file_name);

    if (!input_file.is_open())
    {
        printf("Problem opening file!\r\n");
    }

    while (input_file.is_open() && input_file)
    {
        // Get a new line from the file
        std::string line;
        std::getline(input_file, line);
        
        // Create a stream to get words separated by spaces
        std::istringstream iss(line);
        std::string word;

        // Flag to separate words into the different lists
        bool first_column = true;
        while (iss >> word)
        {
            if (first_column)
            {
                left_list.push_back(std::stoi(word));
                first_column = false;
            }
            else
            {
                right_list.push_back(std::stoi(word));
            }
        }
    }

    return std::make_tuple(left_list, right_list);
}

int main(void)
{
    printf("Starting\r\n");

    auto start = std::chrono::high_resolution_clock::now();

    // Find path of current directory to process the input file
    const std::string file_path = __FILE__;
    const std::string dirPath = file_path.substr(0, file_path.find_last_of("/\\"));
    // auto [left_list, right_list] = parse_lists(dirPath + "/inputs_test.txt");
    auto [left_list, right_list] = parse_lists(dirPath + "/inputs.txt");

    auto end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double, std::milli> duration = end - start;
    printf("Inputs parsing Execution time: %f milliseconds\r\n", duration);

    // Part 1

    start = std::chrono::high_resolution_clock::now();

    // Sort the lists
    std::sort(left_list.begin(), left_list.end());
    std::sort(right_list.begin(), right_list.end());

    std::vector<int> distances;
    int total_distance = 0;
    // Calculate distances
    for (size_t i = 0u; i < left_list.size(); i++)
    {
        const int distance = std::abs(left_list[i] - right_list[i]);
        distances.push_back(distance);
        total_distance += distance;
    }

    end = std::chrono::high_resolution_clock::now();

    duration = end - start;
    printf("Part 1 Execution time: %f milliseconds\r\n", duration);
    printf("total distance: %i\r\n", total_distance);

    // Part 1

    start = std::chrono::high_resolution_clock::now();

    // Count repetitions and store in map
    std::unordered_map<int, int> ocurrences;
    for ( int n : right_list)
    {
        ocurrences[n]++;
    }

    // For the elements of the left list access their frequency and use it to compute the score.
    int similarity_score = 0;
    for ( int n : left_list)
    {
        similarity_score += n * ocurrences[n];
    }

    end = std::chrono::high_resolution_clock::now();

    duration = end - start;
    printf("Part 2 Execution time: %f milliseconds\r\n", duration);
    printf("similarity score: %i\r\n", similarity_score);
}