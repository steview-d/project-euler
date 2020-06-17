def counter(n):
    return(sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0]))


print("Count:", counter(1000))
