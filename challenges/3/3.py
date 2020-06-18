def is_prime(n):
    # check if n is a prime, return bool
    for i in range(2, int(n**(.5))+1):
        if n % i == 0:
            return False
    return True


def prime_list(n):
    # create list of primes up to value n
    prime_list = []
    for i in range(n):
        if is_prime(i):
            prime_list.append(i)
    return prime_list


def prime_factor(n, pl):
    # create list of prime numbers
    prime_nums = prime_list(pl)

    # return largest prime factor by returning
    # 1st value in a reversed list
    for i in reversed(prime_nums):
        if n % i == 0:
            return i


print(prime_factor(600851475143, 10000))
