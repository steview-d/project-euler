def sum_square_diff(n):
    """
    Calculate the difference between the sum of the squares of the
    first n natural numbers and the square of the sum of 1-n.

    Args:
        n (int): The first n numbers to calculate.

    Returns
        (int): Difference between 'sum of the squares'
                 and 'square of the sum'.

    """
    sum_of_squares = sum(x**2 for x in range(1, n+1))
    square_of_sum = sum(range(n+1))**2

    return square_of_sum - sum_of_squares


print(sum_square_diff(100))
