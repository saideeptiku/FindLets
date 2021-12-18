"""
Problem Description:

Identify tuple of 3 elements in an array of integers (positive, negative and zero)
that have sum value of 0. The detected tuples should not have duplicates. 
The output of program should print the identified tuples.

E.g: array = [-5,-2,-5,0,5,5,2]

Output should be -> [-5,0,5], [-2,0,2]
Total -> two tuples
"""
from sys import argv
import numpy as np
# importing the functions that actually do the work
from find_triplets import (
    better_find,
    naive_find,
)

def gen_test_numbers(
        len_lim: int = 10,
        dummy=False,
        default_range=(-99, 99),
):
    """Generate a list of numbers with length N

    Parameters
    ----------
    len_lim : int
        Number of elements in the list
    dummy : bool
        Return the list given in description example
    default_range : tuple
        Tuple describing the range of numbers to consider

    Returns
    -------
    list
        List of integers
    """

    if dummy:
        return [-5, -2, -5, 0, 5, 5, 2]

    return list(
        np.random.randint(
            *default_range,  # min and max numbers
            size=len_lim,  # size upper bound
        ))


def print_results(
    input_nums: list,
    result_tuples: list,
):
    """Function to ensure output format

    Parameters
    ----------
    input_nums: list
        List of integers evaluated
    result_tuples : list
        List of tuples of triplets
    """

    # remove spaces
    preped_input = str(input_nums).replace(" ", "")
    print(f"\narray = {preped_input}\n")

    print(f"Output should be -> ", end="")

    # iter results and format
    for i, (a, b, c) in enumerate(result_tuples):

        print(f"[{a},{b},{c}]", end="")

        if i != len(result_tuples) - 1:
            print(", ", end="")
    print()  # got to next line after printing

    # print total
    print(f"Total -> {len(result_tuples)} tuples")


#####################################################
# Testing Area
#####################################################


def dummy_print_test():
    """Perform a dummy print test
    """
    # numbers to be tested
    test_list = gen_test_numbers(dummy=True)
    results = [(-5, 0, 5), (-2, 0, 2)]

    # print results
    print_results(test_list, results)


#####################################################


def main():
    pass


if __name__ == "__main__":
    if len(argv) == 1:
        print("Performing dummy print test.\n")
        dummy_print_test()
    
    # TODO: if custom input is less than three then abort
    
    main()
