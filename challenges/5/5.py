def smallest_multiple(rng, limit=1000000000):
    """
    Find the smallest positive integer that is evenly divisible
    by all numbers in range 1 through 'rng'

    Args:
        rng (int): The upper limit of range 1-'rng'
        limit (int): (optional) Function will search for a result up to
                     this value.
                     Defaults to 1000000000 (1 billion).

    Returns:
        k (int): The smallest divisible integer
        OR
        (string): To state no number found in given range
    """

    for x in range(5, limit+1, 5):
        for r in range(1, rng+1):
            if x % r != 0:
                break
            elif r == rng:
                return x

    return (f"No number found for range {rng}")


print(smallest_multiple(20))
