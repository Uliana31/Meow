
def myZip(*iterables):
    (*iterators,) = map(iter, iterables)
    while True:
        try:
            result = tuple(next(iterator) for iterator in iterators)
            yield result
        except RuntimeError:
            break
            


            
    
