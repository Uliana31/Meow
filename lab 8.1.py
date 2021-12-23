def print_map(function, iterable,a=iterable.__iter__(),exist=True):
    if exist:
        print(function(a))
        try:
            a=next(a)
        except StopIteration:
            exist=False
        print_map(function,iterable,a, exist)
     
    
 
