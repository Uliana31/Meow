from itertools import permutations
def my_permutations(st, n):
    for i in permutations(st,n):
        print(''.join(i))

st,n=input(), int(input())
my_permutations(st,n)
