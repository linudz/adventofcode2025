#!/usr/bin/env python3

# Advent of code 2025. Day 3.

puzzle = "puzzle.txt"
test = "test.txt"

# Part 1

#  Function read_battery_part1(): reads the battery with part 1 logic (find the two digits with the highest value combined)
def read_battery_part1(battery_string):


    # Import the battery
    battery = [int(x) for x in list(battery_string)]

    # The banks in the battery (unique digits)   
    banks = list(set(battery))

    # Select switch_a (first digit) as the highest value
    switch_a = max(banks)

    # Warning: if the highest value is at the end of the battery, you can't use it as "switch a".
    # Here, we remove it and repeat the switch a identification without it
    switch_a_position = battery.index(switch_a)

    if switch_a_position == len(battery) - 1:
        banks.remove(switch_a)
        switch_a = max(banks)
        switch_a_position = battery.index(switch_a)

    # Let's find the switch b as the highest value at the right of the switch a (rest_of_the_battery)
    rest_of_the_battery = [int(x) for x in battery_string[switch_a_position +1:]]

    switch_b = max(rest_of_the_battery)

    # The joltage is the int value of the sequence "switchAswitchB"
    joltage = int(str(switch_a) + str(switch_b))

    return joltage


def read_battery_part2(battery_string, number_of_digits = 12):
        
        # Import the battery
        battery = [int(x) for x in list(battery_string)]

        # Here, we need to fill a list (digits) with 12 banks
        # We will start:

        digits= []                      # 1) With no digits 
        starting_point = 0              # 2) From the first bank (index=0)
        rest_of_the_battery = battery   # 3) Scanning all the battery from one point on

        # We loop till we have 12 digits. Or while the len(digits) < 12
        while len(digits) < number_of_digits:

            # We slice the rest of the battery from the starting point 
            rest_of_the_battery = rest_of_the_battery[starting_point:]

            # We count how many digits we have left
            digits_left = number_of_digits - len(digits)

            # Eligible banks are those banks which index() in rest_of_the battery
            # is less than the number of digits left to find. In this way, we won't include a number
            # with not enough digits on its right to complete the 12 digits string

            eligible_banks = [bank for bank in list(set(rest_of_the_battery)) if len(rest_of_the_battery) - rest_of_the_battery.index(bank) >= digits_left]

            # Amongst the eligible banks, we chose the highest to maximize the joltage
            digits.append(max(eligible_banks))

            # Here, we update the starting point to keep searching in the next loop
            starting_point = rest_of_the_battery.index(max(eligible_banks)) + 1


        # Joltage is returned as the int of the concatenation of the digits.        
        return int("".join([str(x) for x in digits]))

if __name__ == "__main__":
    with open(test) as handle:

        # Import puzzle
        puzzle = handle.read().splitlines()

        # Part 1: looping over the puzzle to fetch string-per string values and summarizing
        result_part_1 = sum([read_battery_part1(x) for x in puzzle])

        # Part 2: looping over the puzzle to fetch string-per string values and summarizing
        result_part_2 = sum(read_battery_part2(x) for x in puzzle)

        # And we reactivate the elevator :)
        print(f"Result Part 1 {result_part_1}, Result Part 2 {result_part_2}")