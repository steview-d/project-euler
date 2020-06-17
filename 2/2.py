def fibonacci_evens(limit):
    fs = [1, 2]

    while fs[-1] + fs[-2] < limit:
        fs.append(fs[-1] + fs[-2])

    return(sum(n for n in fs if n % 2 == 0))


print(fibonacci_evens(4000000))
