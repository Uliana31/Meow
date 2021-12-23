def mapper(func, *args):
    for i in zip(*args):
        yield func(*i)
