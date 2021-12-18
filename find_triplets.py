"""
Given a list of integers
functions to find 3 triplets that sum to zero

"""

def better_find(numbers: list):
    """A better solution that trades inner most loop for dict

    Time Complexity: O(n^2) # 2 nested loops
    Space Complexity: O(n)  # n elements numbers 

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
    results = []

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
            if third_number != x and third_number != y and third_number in numbers:
                
                # This step ensures that [-5, 0, 5] and [5, 0, -5]
                # are the same thing when hashed later. ie Avoid duplicates
                # Sort a list of constant number of elements
                # is constant time complexity O(3), same for calling tuple
                triplet = tuple(sorted([x, y, third_number]))


                # save the triplet somewhere
                results.append(triplet)


    return set(results)


def naive_find(numbers: list):
    """A naive approach

    This approach looks at all possible compbination of triplets

    Time Complexity: O(n^3) # 3 nested loops
    Space Complexity: O(1)  # no extra space required

    Parameters
    ----------
    numbers : list
        list of numbers to find triplets in

    Returns
    -------
    set
        set of tuples that are triplets
    """

    # sanity check
    if len(numbers) < 3:
        # Could also consider testing if the elements are valid
        # But skipping for now
        print("Warning: should provide atleast 3 numbers")
        # just in case this is called in a loop!
        # let's not raise an exception
        return []

    # triplets will be stored here
    results = []

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
                    results.append(triplet)

    # can be done in O(N)
    # upper bound is still lower
    return set(results)


if __name__ == "__main__":
    print("naive ", naive_find([-5, -2, -5, 0, 5, 5, 2]))
    print("better", better_find([-5, -2, -5, 0, 5, 5, 2]))

