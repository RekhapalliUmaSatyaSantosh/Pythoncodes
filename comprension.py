# a=[x*x for x in range(1,11)]
# print(a)

# a=[x for x in range(0,51,2)]
# print(a)

# a=[x for x in range(1,51,2)]
# print(a)

# a=[i.upper() for i in ['bloody','romeo','king','romardo','lincon','luther']]
# print(a)

# a=[x for x in range(1,100) if x%3==0]
# print(a)

# l=['asdffgtr','sdfgtredf','sdftegij','wijkijijnkijhnmj']
# a=[len(x) for x in l]
# print(a)

# l=[10,1,30,2,53,5,57,9,0,145,8,37]
# a=[x for x in l if x>10]
# print(a)

# import functions as f
# a=(12,13,15,17,19,23,1,2,6,37)
# b=[x for x in a if f.isprime(x)]
# print(b)

# a=(12,13,15,17,19,23,1,2,6,37)
# b=(lambda x: [i for i in range(2,x) if x%i==0])
# l=[i for i in a if not b(i)]
# print(l)

# a=["ODD" if x%2 else 'EVEN' for x in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]]
# print(a)

# a=['Pass' if x>=40 else 'Fail' for x in [45,67,89,91,23,33,55,57,78,21,20,45,56,65]]
# print(a)

# a=[0 if i<0 else i for i in [1,5,-2,-4,2,5,6,-9,0,-9,78,-988]]
# print(a)

# l=[[1,2],[3,4]]
# a=[y for x in l for y in x]
# print(a)

# a={x*x for x in range(1,11)}
# print(a)

# a={x for x in [1,21,2,1,2,3,4,5,4,3,2,1,5]}
# print(a)

# a={x for x in 'kjhgdsaqwertyujkioumnfdsawerg' if x in 'aeiou'}
# print(a)

# a={i:i*i for i in range(1,11)}
# print(a)

# l=['kill','boy','let the men']
# m=['the','johnson','be born']
# a={l[i]:m[i] for i in range(len(l))}
# print(a)

# a={i:i**3 for i in range(1,10) if i%2}
# print(a)

# a={i:'odd' if i%2 else 'Even' for i in range(1,11)}
# print(a)

# import functions as f
# a={i:'prime' if f.isprime(i) else 'Not prime' for i in range(1,51)}
# print(a)


