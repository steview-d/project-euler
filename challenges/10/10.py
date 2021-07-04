def is_prime(n):
    """
    Check if n is a prime

    Args:
        n (int): The value to check

    Returns
        bool: True, if n is a prime

    """

    for i in range(2, int(n**(.5))+1):
        if n % i == 0:
            return False
    return True

def primes_sum(n):
    """
    Find the sum of all the primes below n

    Args:
        n (int)

    Returns
        (int)

    """

    # create a list of all primes below n
    prime_list = []
    for i in range(2, n + 1):
        if is_prime(i):
            prime_list.append(i)

    return sum(tuple(prime_list))


print(primes_sum(2000000))
