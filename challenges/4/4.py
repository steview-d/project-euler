def find_palindrome(num_digits_a, num_digits_b):
    """
    Find the largest palindrome made from the product of two n-digit numbers.

    Args:
        num_digits_a (int): number of digits in number
        num_digits_b (int): number of digits in number

    Returns:
        largest (int): The largest palindrome found
    """

    a, b = 10**num_digits_a-1, 10**num_digits_b-1
    largest = 0

    for x in range(a, 0, -1):
        for y in range(b, 0, -1):
            if is_palindrome(x*y) and x*y > largest:
                largest = x*y
    return largest


def is_palindrome(n):
    """
    Check if n is a palindrome

    Args:
        n (int): The number to check

    Returns: Boolean
    """

    # get number of digits in n, halved
    h = int(len(str(n)) / 2)

    return True if str(n)[:h] == str(n)[:-h-1:-1] else False


print(find_palindrome(3, 3))
