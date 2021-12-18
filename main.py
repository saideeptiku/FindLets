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
"""
from sys import argv
# from test import test_triplet_finder
# importing the functions that actually do the work
from find_triplets import (
    better_find,
    naive_find,
)



def main():
    pass


if __name__ == "__main__":
    # if len(argv) == 1:
    #     print("Performing dummy print test.\n")
    #     dummy_print_test()
    #     exit()

    # test_naive_better()    


    # TODO: if custom input is less than three then abort
    
    main()
