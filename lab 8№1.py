from itertools import product
def get_product(arg1, arg2):
    data=list(product(arg1, arg2))
    print(data)

a,b=input(), input()
get_product(a,b)
    
