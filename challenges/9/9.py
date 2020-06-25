def pythagorean_triplet_list(n):
    """
    Find the Pythagorean triplet for which a + b + c = 1000
    and return the product of abc

    Args:
        n (int): maximum c value

    Returns
        (int): product of abc

    """

    triplet_list = []

    for c in range(1, n):
        for b in range(1, c):
            for a in range(1, b):
                if a**2 + b**2 == c**2:
                    triplet_list.append([a, b, c])

    for x in triplet_list:
        if(sum(x)) == 1000:
            return (x[0] * x[1] * x[2])

    return "Not Found!"


print(pythagorean_triplet_list(440))
