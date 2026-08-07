# a=map(lambda x,y:x*y,[1,2,3],[4,5,6])
# print(list(a))

# m1=[[1,2,3],
#     [4,5,6],
#     [7,8,9]]
# m2=[[1,2,3],
#     [4,5,6],
#     [7,8,9]]
# r=[]
# for i in range(len(m1)):
#     a=map(lambda x,y:x+y,m1[i],m2[i],strict=True)
#     r.append(list(a))
# print(r)

'''We can also pass keyword argument strict which gives an error if the size of iterables is not equal.
We can use strict argument in python version 3.14+.
Filter: It is used to filter elements on the function return value.
syntax: filter(function,iterable)
In order to access the filter object, we need to loop or typecast
'''

# a=filter(lambda x:x%2,[12,3,4,8,11,19,18])
# print(list(a))

# a=['username','password']
# b=['asp','123']
# x=map(lambda x,y:(x,y), a,b)
# print(dict(x))

# a=['Akshaya','Aishwarya','Akash','Kiran']
# x=filter(lambda x: x[0].lower()=='a',a)
# print(list(x))

# l=[1,2,3,4,5,6,6,7]
# a=sum(l)/len(l)
# x=filter(lambda x: x<a,l)
# print(list(x))

l=['a','','b','','c']
x=filter(lambda x:x!='',l)
print(list(x))