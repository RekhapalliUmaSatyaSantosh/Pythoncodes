# my_tuple=(1,2,3,4,5)
# my_list=[6,7]
# a=tuple(my_list)
# a=my_tuple+a
# b=list(a)
# # print(a)
# print(b)

# tuple=('ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE')
# num = int(input("Enter a number between 0 to 9:"))
# print(tuple[num])

# tuple1=(1,2,3,4,5)
# print(len(tuple1))


# t1=(10,200,4,6,23,35,9,30)
# t2=(30,40,50)
# print(t1<t2)
# print(t1<=t2)
# print(t1>t2)
# print(t1>=t2)
# print(70 not in t1)
# t=sorted(t1)
# t2=tuple(t)
# print(t)

# l=(10,20,30,40)
# a,b,*d=l
# print(a,b,d)

# a=10
# b=20
# c=30
# l=a,b
# print(l)

# l=(x*x for x in range(1,6))
# l1=tuple(l)
# print(l1)
# print(type(l))

t=eval(input("enter elements of tuple:"))
t1=sum(t)
t2=sum(t)/len(t)
print(t1)
print(t2)