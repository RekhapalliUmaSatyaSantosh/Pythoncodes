##a=6
##for i in range(1,a):
##    for j in range(i,a-1):
##        print(' ',end=' ')
##    for k in range(i,0,-1):
##        print(k,end=' ')
##    print()

##for i in 'hello':
##    print(i)

##for i in [1,2,3,4,3,2,1]:
##    print(i)

##l=eval(input())
##l1=[]
##for i in l:
##     l1.append(i)
##     l1.sort()
##print(l1[-1])

##l=[1,2,3,284,93828,402013,193,84,1094,43]
##h=l[1]
##for i in l:
##    if i>h:
##        h=i
##print(h)

##l=[11121,2,3,284,9388,402013,193,84,1094,43]
##h=l[1]
##sh=None
##for i in l:
##    if i>h:
##        sh=h
##        h=i
##    elif sh==None:
##        if h!=1:
##            sh=i
##    elif sh<i<h:
##        sh=i
##print(sh)

##for i in range(1,11):
##    print(i,end=' ')

##for i in range(2,51,2):
##    print(i)

##n=int(input())
##l=0
##for i in range(1,n+1):
##    l+=i
##print(l)

##n=int(input())
##for i in range(1,21):
##    print(n,'x',i,'=',n*i)

##n=eval(input())
##for i in range(1,len(n),2):
##    print(n[i])

#rotate list upto k positions
##n=eval(input())
##k=3
##for i in range(k):
##    l=n.pop()
##    n.insert(0,l)
##print(n)

##n=[9,-1,1,4,5,7,2,3,6,8]
##t=8
##r=set()
##for i in n:
##    if (t-i) in r:
##        print((i,(t-i)),end=' ')
##    r.add(i)  

#missing element from 1-n range
##n=eval(input())
##for i in range(1,len(n)+1):
##    if i not in n:
##        print(i)

#missing element from 1-n range if more nums are missing side by side
##n=eval(input())
##h=n[0]
##for i in n:
##    if i>h:
##        h=i
##for i in range(1,h):
##    if i not in n:
##        print(i)

##l=eval(input())
##l1=[]
##for i in l:
##    if i in l1:
##        print(i)
##    else:
##        l1.append(i)
##print(l1)

#to check numbers present in list sum to prime number
##n=eval(input())
##s=0
##flag=True
##for i in n:
##    s+=i
##for i in range(2,s):
##    if s%i:
##        flag=False
##if flag:
##    print('Not Prime')
##else:
##    print('prime')

##n=input()
##c=0
##for i in n:
##    c+=int(i)
##print(c)

##n=input()
##h=n[0]
##for i in n:
##    if i>h:
##        h=i
##print(h)

##n=input()
##m=input()
##c=0
##for i in n:
##    if m in i:
##        c+=1
##print(c)

##n=input()
##res=''
##for i in n:
##    res=i+res
##print(res)

n=input()
res=''
for i in n:
    res=i+res
    print(res)
if n==res:
     print('palindrome')
else:
    print('Not palindrome')

#second highest number
##n=input()
##h=-1
##sh=-1
##for i in n:
##    d=int(i)
##    if d>h:
##        sh=h
##        h=d
##    elif d>sh and h!=d:
##        sh=d
##print(sh)

#armstrong number
##n=input()
##res=0
##p=len(n)
##for i in n:
##    d=int(i)
##    res+=d**p
##print(res)

#sum of even and odd indices
##n=input()
##odd=0
##even=0
##for i in n:
##    d=int(i)
##    if d%2==0:
##        even+=d
##    else:
##        odd+=d
##print('Even=',even)
##print('Odd',odd)

#nonrepeated char in a string
##n=input()
##for i in n:
##    if n.count(i)==1:
##        print(i)

##n=input()
##res=0
##for i in n:
##    d=int(i)
##    if d%2==0:
##        res+=d
##print(res)

##n=input()
##c=0
##for i in n:
##    c+=1
##print(c)

##n=input()
##c=0
##for i in n:
##    if i.lower() in ['a','e','i','o','u']:
##        c+=1
##print(c)

##n=int(input())
##fact=1
##for i in range(1,n+1):
##    fact*=i
##print(fact)

##n=eval(input())
##for i in range(0,len(n),2):
##    print(n[i],end=' ')

