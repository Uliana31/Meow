
def fib():
    a=1
    b=1
    while True:
        yield a
        a,b=b, a+b
n=int(input())
gen = fib()
for i in range(n):
    print(next(gen))
