def prime_list(n):
    """
    Find & return the n-th prime number

    Args:
        n (int): n-th prime to return

    Returns
        (int): value of n-th prime
    """

    prime_list = []
    count = 2
    while len(prime_list) < n:
        if is_prime(count):
            prime_list.append(count)
        count += 1

    return prime_list[-1]


def is_prime(n):
    # check if n is a prime, return bool
    for i in range(2, int(n**(.5))+1):
        if n % i == 0:
            return False
    return True


print(prime_list(10001))
