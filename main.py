"""
Problem Description:

Identify tuple of 3 elements in an array of integers (positive, negative and zero)
that have sum value of 0. The detected tuples should not have duplicates. 
The output of program should print the identified tuples.

E.g: array = [-5,-2,-5,0,5,5,2]

Output should be -> [-5,0,5], [-2,0,2]
Total -> two tuples


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

def print_help():
    print("""
    python3 main.py [--naive|--better] --numbers=50 --file=inputs.csv --gen_file

    ARGS:
    ----
    --naive: A naive approach with time complexity O(n^3).
    --better: Improved approach with time complexity O(n^2).
    --gen_file: Only generates inputs.csv file. Overrides all other flags.

    KWARGS:
    -------
    --numbers (default=50): Generate 50 numbers between -99 to 99 and print unique triplets.
    --file (default=input.csv): A file where each line has comma separated numbers.
                                Overrides --number flag.

    Example: 

    """)


def main():
    print_help()


if __name__ == "__main__":
    # if len(argv) == 1:
    #     print("Performing dummy print test.\n")
    #     dummy_print_test()
    #     exit()

    # test_naive_better()    


    # TODO: if custom input is less than three then abort
    
    main()
