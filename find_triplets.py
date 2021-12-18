"""
Given a list of integers
functions to find 3 triplets that sum to zero

Notes:
1. Traded in constant time improvement for readability and 
my own implementation speed (time taken to implement code)

2. functionally space complexity of both solutions is same O(n)
   both naive_find and better_find maintain a set of length O(n),
   where n is the unique number of elements in numbers list 
"""

def better_find(numbers: list):
    """A better solution that trades inner most loop for dict

    Time Complexity: O(n^2) # 2 nested loops
    See note on space complexity under file summary

    Parameters
    ----------
    numbers : list
        list of numbers to find triplets in

    Returns
    -------
    set
        set of tuples that are triplets
    """

    # store results here
    results = set([])

    # considering duplication of a number has no impact on output
    # and also makes traking of numbers easy
    # ignore repeating numbers
    numbers = set(numbers)
    # Operation above has complexity O(n)
    # Has additive effect with rest of the algorithm

    for i, x in enumerate(numbers):
        for j, y in enumerate(numbers):
            
            # avoid summing to self
            # Note: this can be avoided with better iteration
            #       Will make some constant time improvement
            #       I think this has better readability
            if i == j:
                continue

            # sum of two numbers
            two_sum = x + y 
            # determine third number required to make two_sum zero 
            third_number = 0 - two_sum
            # check if third number is in hashing table or set
            # below is a constant time operation
            # link about sets O(1) key check in python https://qr.ae/pGqLf4
            # Could have made a dict object for safety also
            if third_number != x and third_number != y and third_number in numbers:
                
                # This step ensures that [-5, 0, 5] and [5, 0, -5]
                # are the same thing when hashed later. ie Avoid duplicates
                # Sort a list of constant number of elements
                # is constant time complexity O(3), same for calling tuple
                triplet = tuple(sorted([x, y, third_number]))


                # save the triplet somewhere
                results.add(triplet)

    # can be done in O(N)
    # remove recurring finds
    return results


def naive_find(numbers: list):
    """A naive approach

    This approach looks at all possible compbination of triplets

    Time Complexity: O(n^3) # 3 nested loops
    See note on space complexity under file summary

    Parameters
    ----------
    numbers : list
        list of numbers to find triplets in

    Returns
    -------
    set
        set of tuples that are triplets
    """

    # getting rid of repeating numbers
    # does not have impact on output in example
    numbers = set(numbers)

    # sanity check
    if len(numbers) < 3:
        # Could also consider testing if the elements are valid
        # But skipping for now
        print("Warning: should provide atleast 3 numbers")
        # just in case this is called in a loop!
        # let's not raise an exception
        return set([])

    # triplets will be stored here
    results = set([])

    for i, x in enumerate(numbers):
        for j, y in enumerate(numbers):
            for k, z in enumerate(numbers):

                # avoid summing to self
                # Note: this can be avoided with better iteration
                #       Will make some constant time improvement
                #       I think this has better readability
                if i == j or j == k or i == k:
                    continue
                    # skip the check below

                # check if sums to one
                if x + y + z == 0:
                    # This step ensures that [-5, 0, 5] and [5, 0, -5]
                    # are the same thing when hashed later. ie Avoid duplicates
                    # Sort a list of constant number of elements
                    # is constant time complexity O(3)
                    triplet = tuple(sorted([x, y, z]))

                    # save the triplet somewhere
                    results.add(triplet)

    # return results
    return results


if __name__ == "__main__":
    print("naive ", naive_find([-5, -2, -5, 0, 5, 5, 2]))
    print("better", better_find([-5, -2, -5, 0, 5, 5, 2]))

