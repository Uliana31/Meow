from itertools import combinations_with_replacement
def my_combinations_with_r(s,k):
    for i in combinations_with_replacement(s,k):
        print(''.join(i))


s,k=input(), int(input())
my_combinations_with_r(s,k)
