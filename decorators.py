# def dec(func):
#     return print
# @dec
# def add(a,b):
#     return a+b
# add(10,20)

# def welcome(func):
#     def inner(a,b):
#         print('Hai hello')
#         return func(a,b)
#     return inner
# @welcome
# def add(a,b):
#     return a+b
# @welcome
# def sub(a,b):
#     return a-b
# a=add(10,20)
# b=sub(20,10)
# print(a,b)

import time

def welcome(n):
    def inner(a,b):
        start=time.time()
        print('start')
        print(n(a,b))
        print('end')
        end=time.time()
        print(end-start)
    return inner
@welcome
def add(a,b):
    return a+b
add(10,20)
