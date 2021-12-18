"""
Functions used for testing this module
"""

from helper import print_results, gen_test_numbers
from tqdm.auto import tqdm
from find_triplets import better_find, naive_find
from typing import Callable

def dummy_print_test():
    """Perform a dummy print test
    """
    # numbers to be tested
    test_list = gen_test_numbers(dummy=True)
    results = set([(-5, 0, 5), (-2, 0, 2)])

    # print results
    print_results(test_list, results)


def test_triplet_finders():
    """see if naive_find and better_find work the same way
    """

    # iterate over possible length of list passed to our functions
    for len_nums in [10, 100, 1_000, 10_000]:
        print(f"list size:", len_nums)
        # test on same number 10 times
        for _ in tqdm(range(10)):
            # gen some list of numbers
            numbers = gen_test_numbers(len_nums)

            naive_set = naive_find(numbers)
            better_set = better_find(numbers)

            if naive_set != better_set:
                print("ERROR!")
                print(numbers)
                print("NAIVE")
                print(naive_set, len(naive_set))
                print("BETTER")
                print(better_set, len(better_set))

                print("DIFF")
                if len(naive_set) > len(better_set):
                    print(naive_set - better_set)
                else:
                    print(better_set - naive_set)

                exit()


def timed_test(finder: Callable):
    """return the run time of a function under different conditions
    """

    # iterate over possible length of list passed to our functions
    for len_nums in [10, 100, 1_000, 10_000]:
        print(f"list size:", len_nums)
        # test on same number 10 times
        for _ in tqdm(range(10)):
            # gen some list of numbers
            numbers = gen_test_numbers(len_nums)

            triplet_set = finder(numbers)



if __name__ == "__main__":
    print("1. Test printing function")
    dummy_print_test()
    print("## 1. END ##\n")
    print("2. Test functionality.")
    # Assumes one of the two implementations are functionally correct
    test_triplet_finders()
    print("## 2. END ##\n")
    print("3. Make Time Plot")
    print("## 3. END ##\n")

