"""
Problem Description:

Identify tuple of 3 elements in an array of integers (positive, negative and zero)
that have sum value of 0. The detected tuples should not have duplicates. 
The output of program should print the identified tuples.

E.g: array = [-5,-2,-5,0,5,5,2]

Output should be -> [-5,0,5], [-2,0,2]
Total -> 2 tuples


Notes:
- Tested with python3 == 3.8 (>= 3.6)
              numpy == 1.21.2
              tqdm == 4.62
              matplotlib == 3.5.1
"""
from sys import argv
# importing the functions that actually do the work
from find_triplets import (
    better_find,
    naive_find,
)
from helper import gen_test_numbers, print_results
import numpy as np
from typing import Callable


def print_help():
    print("""
    python3 main.py [--naive|--better] --numbers 50 --from_file inputs.csv --gen_file inputs.csv

    ARGS:
    ----
    --naive: A naive finder approach with time complexity O(n^3).
    --better: Improved finder approach with time complexity O(n^2).
    --help: prints this msg.

    KWARGS:
    -------
    --numbers: Generate N numbers between -9 to 9 and print unique triplets.
    --from_file: A file where each line has comma separated numbers.
                                Overrides --number flag.
    --gen_file: Only generates a file. Overrides all other flags. Does not execute the finders.
                Example: Following command will generate inputs.csv file with 10 rows and 30 cols
                python3 --genfile inputs.csv 10 30 

    Example: 

    python3 main.py --better numbers 30

    """)


def gen_file(file_name: str, r: int, c: int):
    """generate inputs.csv with 3 lines
    and numbers ranging between -9 to 9
    """
    np_array = np.random.randint(-9, 9, (r, c))
    # save the array as a text file
    np.savetxt(
        file_name,
        np_array,
        delimiter=",",
        fmt="%d",
    )


def from_file(file_name: str, finder: Callable):
    """read csv file as list of list

    Parameters
    ----------
    file_name : str
        csv file with integers
    """
    # read file
    np_array = np.genfromtxt(file_name, delimiter=",").astype(int)

    # read each line from file and call finder on line
    for line in np_array:
        numbers = list(line)
        triplets = finder(numbers)
        print_results(numbers, triplets)


def main():
    # An overly simple arg parser
    if "--help" in argv:
        print_help()

    # if generate file; ignore everything else
    elif "--gen_file" in argv:
        file_name = argv[argv.index("--gen_file") + 1]
        rows = int(argv[argv.index("--gen_file") + 2])
        cols = int(argv[argv.index("--gen_file") + 3])
        gen_file(file_name, rows, cols)

    # evaluate tuples from a file provided
    elif "--from_file" in argv:
        # check if naive or better was asked for
        # get item after --from_file
        file_name = argv[argv.index("--from_file") + 1]
        if "--naive" in argv:
            from_file(
                file_name,
                naive_find, # function to call
            )
        elif "--better" in argv:
            from_file(
                file_name,
                better_find,
            )
        else:
            print_help()
            exit("Finder not provided! See help above.")

    # generate and test numbers at the same time
    elif "--numbers" in argv:
        # extract numbers wanted
        num_len = int(argv[argv.index("--numbers") + 1])
        # gen numbers
        numbers = gen_test_numbers(num_len, default_range=(-9, 9))
        # call and exec naive or better
        if "--naive" in argv:
            print_results(numbers, naive_find(numbers))
        elif "--better" in argv:
            print_results(numbers, better_find(numbers))
        else:
            print_help()
            exit("Finder not provided! See help above.")
    
    # nothing matched? print help and exit with msg
    else:
        print_help()
        exit("Invalid input! See help above.")


if __name__ == "__main__":
    main()
