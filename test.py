"""
Functions used for testing and evaluation of this module
"""

from helper import print_results, gen_test_numbers
from tqdm.auto import tqdm
from find_triplets import better_find, naive_find
from typing import Callable
from time import time
from matplotlib import pyplot as plt

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
    Assumes one of the two implementations are functionally correct
    """

    # iterate over possible length of list passed to our functions
    for len_nums in [10, 100, 1_000]:
        print(f"list size:", len_nums)
        # test on same number 5 times
        for _ in tqdm(range(5)):
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

                return


def timed_test(finder: Callable):
    """return the run time of a function under different conditions

    Parameters
    ----------
    finder : Callable
        Takes input a list of numbers and returns set of triplets
    """

    final_times = []

    # iterate over possible length of list passed to our functions
    for len_nums in [10, 100, 1_000]:
        print(f"list size:", len_nums)
        times = []

        # test on same number 5 times
        for _ in tqdm(range(5)):
            # gen some list of numbers
            numbers = gen_test_numbers(len_nums)

            # curr time
            t = time()
            _ = finder(numbers)  # execute, no need to save
            # save elasped time
            times.append(time() - t)

        # take avg and save
        final_times.append(sum(times) / 5)

    return final_times


if __name__ == "__main__":
    print("1. Test printing function")
    dummy_print_test()
    print("## 1. END ##\n")

    print("2. Test functionality.")
    test_triplet_finders()
    print("## 2. END ##\n")

    print("3. Make Time Plot. See times.png file.")
    naive_times = timed_test(naive_find)
    better_times = timed_test(better_find)
    print("naive: ", naive_times)
    print("better:", better_times)
    # plot results
    plt.plot(naive_times, label="Naive O(n^3)")
    plt.plot(better_times, label="Better O(n^2)")
    plt.legend()
    plt.xlabel("Iters")
    plt.ylabel("Time (seconds)")
    plt.title("Execution Times")
    plt.savefig("times.png")
    # TODO: make the plot; creates another dependency :/
    print("## 3. END ##\n")
