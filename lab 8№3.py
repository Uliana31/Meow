from itertools import combinations
def my_combinations(s,k):
    for i in range(k+1):
        data=list(combinations(s,i))
    print(data)

s,k=input(),int(input())
my_combinations(s,k)
            
