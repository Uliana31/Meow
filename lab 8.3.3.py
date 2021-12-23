def my_enumerate(iterable, start = 0):
    n = len(iterable) - start
    for i in range(n):
        yield tuple(i, iterable[start + i])
