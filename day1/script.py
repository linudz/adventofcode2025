#!/usr/bin/env python3

# Fabio Barteri - Advent of Code 2025

# Day One.

# Open the puzzle
with open("test.txt", "r") as h:
    l = h.read().splitlines()

# Fetching the instructions (L will return a negative value, R a positive one)
instructions = [int(x[1:]) * -1  if x[0] == "L" else int(x[1:]) for x in l]

# The counter for the two questions
zeros_positions = 0                 # Part 1: How many 0s you find as steps
zeros_crossed = 0                   # Part 2: Hou many times you cross the 0


# Start the loop (starting position: 50)
pos = 50

for x in instructions:

    # Correct the absolute value
    original_number = x
    absval = abs(x)

    while absval > 99:
        absval = absval - 100
        zeros_crossed += 1           # Part 2: Crossing the 0 (once for each full round)
    
    step = absval
    
    if original_number < 0:
        step = step * -1
    
    # Calculating the zeroes (positions and crossed)
    crossing_zero = False

    start = pos                 # The starting point. If == 0, I don't count the 0 crossing
    pos = pos + step

    # Crossing 0 left to right
    if pos > 99:
        pos = pos - 100

        if start != 0:
            crossing_zero = True

    # Crossing 0 right to left
    elif pos < 0:
        pos = 100 - abs(pos)

        if start != 0:
            crossing_zero = True

    # Part 1: Count the crossing positions
    if pos == 0:
        zeros_positions += 1
        crossing_zero = True
    # Part 2: Count the zero crossings
    if crossing_zero:
        zeros_crossed += 1
        

print(f"Part 1: {zeros_positions} positions with 0\nPart 2 {zeros_crossed} times crossing 0")





