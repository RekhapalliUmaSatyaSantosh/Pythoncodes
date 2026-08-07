##def add(a,b):
##    '''Hello this is python class'''
##    c=a+b
##    d=a*b
##    e=a/b
##    f=a//b
##    g=a**b
##    h=a%b
##    print(f'add={c},minus={d},mult={e},div={f},floor={g},mod={h}'
##print(add(10,20))
##a=add(10,20)
##print(a)
##a=add
##print(a(10,20))
##print(a.__doc__)

##def add(a,b):
##    print(a+b
##    print(a
##print(add(10,20))

##def isprime(n):
##    for i in range(2,n):
##        if n%i==0:
##            print(False
##    print(True
##print(isprime(23))

##a=[[1,2,3],
##   [1,2,3]]
##b=[[1,2,3],
##   [1,2,3]]
##def validate(m1,m2):
##    if len(m1)!=len(m2):
##        print(False
##    for i in range(len(m1)):
##        if not (len(m1[i]) == len(m2[i]) and len(m1[i]) == len(m1[0])):
##            print(False
##    print(True
##print(validate(a,b))

##def validate(r,c):
##    res=[]
##    for _ in range(r):
##        a=input('Enter a matrix values=').split(',')
##        if c != len(a):
##            print('Not valid'
##        x=[]
##        for i in a:
##            x.append(int(i))
##        res.append(x)
##    print(res
##print(validate(2,2))

##r=int(input('enter rows='))
##c=int(input('enter columns='))
##res=[]
##for _ in range(r):
##    a=input('Enter a matrix values=').split(',')
##    if c != len(a):
##        print('Not valid')
##    x=[]
##    for i in a:
##        x.append(int(i))
##    res.append(x)
##print(res)

##l=['12','3456','789012']
##for i in l:
##    if len(i)%2==0:
##        print('even length=',i)
##    else:
##        print('Not in even length=',i)

# def isprime(n):
#    if n==1:
#        return 'Not prime'
#    else:
#        for i in range(2,n):
#            if n%i==0:
#                return 'Not prime'
#        return 'Prime'
##print(isprime(1))

# def isprime(n):
#    if n==1:
#        return False
#    for i in range(2,n):
#        if n%i==0:
#            return False
#    return True
##n=4
##c=1
##for i in range(n):
##    c2=0
##    l=[]
##    while c2<=i:
##        if not isprime(c):
##            l.append(c)
##            c2+=1
##        c+=1
##    if i%2==0:
##        print(*l)
##    else:
##        print(*l[::-1])

##def num(*n):
##    for i in n:
##        if not isinstance(i,int):
##            print('Not a int'
##    print(n
##a=num(10,20,40,50,'hello')
##print(a)
##
##b=num(10,20,30)
##print(b)

##def val(**n):
##    for i in n.items():
##        print(i)
##val(name='satya',phno=1246808532,email='yourname@gmail.com',age=22)

##def cal(oper,*n):
##    r=n[0]
##    for i in n:
##        if oper=='+':
##            r+=i
##        elif oper=='-':
##            r-=i
##        elif oper=='*':
##            r*=i
##        elif oper=='/':
##            r/=i
##        elif oper=='//':
##            r//=i
##        elif oper=='%':
##            r%=i
##    return r
##            
##print(cal('-',10,20,30,40))

##def info(tag,text='',sc=True,*n,**m):
##    res='<'+tag
##    for i in m:
##        res+=f" {i}='{m[i]}' "
##    for i in n:
##        res+=f'{i} '
##    if sc:
##        res+='>'
##    else:
##        res+=f'>{text} </tag>'
##    print(res)
##info('a','click me',False,href='www.google.com',style='border: 2px solid;')
##
##info('input','',True,'hidden','required',type='text',placeholder='enter a text')

##def info(a,b,c,d):
##    print('a=',a,'b=',b,'c=',c,'d=',d)
##a=[1,2,3,4]
##info(*a)

##a=10
##def outer():
##    global a
##    a+=1
##    print(a)
##    x=10
##    def inner():
##        print(x)
##        x+=1
##        print(x)
##    inner()
##outer()

##def gcd(a,b):
##    h=0
##    for i in range(1,b+1):
##        if a%i==0 and b%i==0:
##            h=i
##    return h
##
##def lcm(a,b):
##    return (a*b)//gcd(a,b)
##print(lcm(10,10))

# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(299))


##def sn(n):
##    res=0
##    for i in str(n):
##        fact=1
##        d=int(i)
##        for j in range(1,d+1):
##            fact*=j
##        res+=fact
##    return n==res
##print(sn(145))

# def ispalindrome(n):
#     r=''
#     m=n.replace(' ','').lower()
#     for i in m:
#         r=i+r
#     if m==r:
#         return True
#     else:
#         return False
# print(ispalindrome('A man a plan a canal Panama'))

# def common(a,b):
#     m=[]
#     for i in a:
#         if i in b and i not in m:
#             m.append(i)
#         m.sort()
#     return m
# print(common([1, 6, 3, 4], [3, 4, 5, 6]))

# def isfibonacci(n):
#     a,b=0,1
#     for _ in range(n):
#         print(a,end=' ')
#         a,b=b,a+b
# isfibonacci(10)

# l=[[1, 4], [2, 5], [7, 9], [8, 10]]
# l.sort()
# r=[]
# for i,j in l:
#     if not r or i>r[-1][1]:
#         r.append([i,j])
#         print(r)
#     else:
#         r[-1][1]=max(r[-1][1],j)
#         print(r)
# print(r)

# def wish(name,greet='Hello'):
#     print(greet,name)
    
# wish('suresh','Goodmorning')

# def sum(*n):
#     r=0
#     for i in n:
#         r+=i
#     return r
# print(sum())

# def details(**n):
#     for i in n:
#         print(i,':',n[i])
# details(name='Alice',age=25,city='New York')

# a=10
# def m():
#     global a
#     a=20
#     print(a)
# m()
# print(a)

# def create_profile(name, age, country="Unknown", *hobbies, **extra):
#     return {
#         'name': name,
#         'age': age,
#         'country': country,
#         'hobbies': hobbies,
#         'extra': extra
#     }
# result = create_profile("Alice", 25, "USA", "reading", "swimming", job="engineer", pet="cat")
# print(result)

# def power(n,p):
#     if p==0:
#         return 1
#     else:
#         return n*power(n,p-1)
# print(power(5,1))

# def count(n):
#     if n<10:
#         return 1
#     else:
#         return 1+count(n//10)
# print(count(123456))

# def reverse(n):
#     m=n
#     if m=='':
#         return ''
#     else:
#         return reverse(m[1:])+m[0]
# print(reverse('malayalam'))

# def fib(n):
#     if n<=1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)
# print(fib(10))