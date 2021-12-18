"""
Functions for generating and printing information
or any other functions that may be generally useful
"""

import numpy as np

def gen_test_numbers(
        len_lim: int = 10,
        dummy: bool = False,
        default_range: tuple = (-99, 99),
):
    """Generate a list of numbers with length N

    Parameters
    ----------
    len_lim : int
        Number of elements in the list
    dummy : bool
        Return the list given in description example
    default_range : tuple
        Tuple describing the range of numbers to consider.
        Increasing this will increase execution times for functions.

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