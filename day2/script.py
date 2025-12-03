#!/usr/bin/env python3

# Advent of code, Day 2.

# Inputs
puzzle = "puzzle.txt"
test = "test.txt"

# Function import_ranges(): imports all the ranges from the puzzle
def read_ranges(filepath):
    with open(filepath) as h:
        range_list = h.read().split(",")
    intervals = {x : [str(number) for number in range(int(x.split("-")[0]), int(x.split("-")[1]) + 1)] for x in range_list}
    return intervals

# Function fetch_repetitions(): it divides a string into chuncs
def fetch_tandem_repetitions(input_string, mode = "part1"):
    flag = False

    # Part 1: we need to find those numbers who are 2 repetitions of
    #         the same number in tandem (e.g. 123123 (123 - 123))
    if mode == "part1":

        # Step 1: exclude odd strings
        if len(input_string) % 2 > 0:
            return flag
        
        # Step 2: slice the string in two

        half = int(len(input_string)/2)

        subA = input_string[:half]
        subB = input_string[half:]

        if subA == subB:
            flag = True

        return flag
    
    # Part 2: we need to find all those numbers that are completely formed with repetitions
    #         even in number > 2. (e.g. 121212, 123123, 121412141214)
    elif mode == "part2":
        import textwrap

        # Step 1: fetch the dividends
        dividends = [x for x in range(1,len(input_string)) if len(input_string) % x == 0]
        
        # Step 2: fetch those cases in which a tandem repeat of any size constitutes the whole string
        #         For each string, I slice into chunks of different sizes e.g. "123123" [[1,2,3,1,2,3], [12,31,23], [123,123]]
        #         This case is detected whenever a set() of the list of chunks has len = 1 e.g. len(set([123,123])) = 1
        tandem_repeats = [set(textwrap.wrap(input_string, x)) for x in dividends if len(set(textwrap.wrap(input_string, x))) == 1]
    
        # Flag is true if even 
        if len(tandem_repeats) > 0:
            flag = True       
        return flag

# Function fetch_invalid_ids(): it scans a range to fetch the invalid ids
def fetch_invalid_ids(range_dictionary, part = "part1"):
    invalid_ids = {key: [x for x in value if fetch_tandem_repetitions(x, part)] for key,value in range_dictionary.items()} 
    return invalid_ids

if __name__ == "__main__":
    
    input_ranges = read_ranges(test)

    # Part 1
    invalid_ids_part1 = fetch_invalid_ids(input_ranges, "part1")
    all_invalids_part1 = [sum([int(n) for n in x]) for x in invalid_ids_part1.values() if len(x) > 0]
    
    # Part 2
    invalid_ids_part2 = fetch_invalid_ids(input_ranges, "part2") 
    all_invalids_part2 = [sum([int(n) for n in x]) for x in invalid_ids_part2.values() if len(x) > 0]

    # Print the result
    print(sum(all_invalids_part1), sum(all_invalids_part2))