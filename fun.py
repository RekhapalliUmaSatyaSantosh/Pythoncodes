# def add(a,b):
#     print(a+b)
# add(10,20)

# def sqrt(num):
#     sqr=num*num
#     print(f'the sqrt of {num} is {sqr}')
# sqrt(4)

# def oper(a,b):
#     sum=a+b
#     minus=a-b
#     multi=a*b
#     div=a/b
#     return sum,minus,multi,div
# t=oper(10,20)
# print(t)
# print(type(t))

# def wish(name='guest'):
#     print('hello',name,'good morning')
# wish('satya')

# def sum(*n):
#     tot=0
#     for i in n:
#         tot=tot+i
#     print(tot)
# sum(10,20,30)

# def f(**n):
#     print(type(n))
# f()

# def friends_in_trouble(j_angry, s_angry):
#     if j_angry=='angry' and s_angry=='angry':
#         return True
#     else:
#         return False
# output=friends_in_trouble('angry','angry')
# print(output)

def transform_string(s):
    if '_' in s:
        parts = s.split('_', 1)
        reversed_part1 = parts[0][::-1]
        return reversed_part1 + '_' + parts[1]
    else:
        return s