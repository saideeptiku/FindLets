"""
Functions used for testing this module
"""

from helper import print_results, gen_test_numbers
from tqdm.auto import tqdm
from time import time
from typing import List, Callable


def dummy_print_test():
    """Perform a dummy print test
    Tests the print_results function
    """
    # numbers to be tested
    test_list = gen_test_numbers(dummy=True)
    results = [(-5, 0, 5), (-2, 0, 2)]

    # print results
    print_results(test_list, results)


def test_triplet_finders(finder_fns: List[Callable]):
    """see if naive_find and better_find work the same way
    """
    # attempting to keep testing import boxed in
    # just a progress bar

    # iterate over possible length of list passed to our functions
    for len_nums in [10, 100, 1_000, 10_000]:
        # test on same number 10 times
        for _ in tqdm(range(10)):
            numbers = gen_test_numbers(len_nums)

            triplet_set = finder_fns[0](numbers)

            # if naive_set != better_set:
            #     print("ERROR!")
            #     print(numbers)
            #     print("NAIVE")
            #     print(naive_set, len(naive_set))
            #     print("BETTER")
            #     print(better_set, len(better_set))

            #     print("DIFF")
            #     if len(naive_set) > len(better_set):
            #         print(naive_set - better_set)
            #     else:
            #         print(better_set - naive_set)

            #     exit()
