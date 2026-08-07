def fib(n):
    a,b=0,1
    for _ in range(n+1):
        yield(a)
        a,b=b,b+a
a=fib(10)
print(list(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))