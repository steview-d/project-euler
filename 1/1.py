def counter(num):
    count = 0
    for i in range(1, num):
        if i % 3 == 0 or i % 5 == 0:
            count += i
    return count


print("Count:", counter(1000))
