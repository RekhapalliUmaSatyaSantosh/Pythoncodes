##for i in range(4):
##    for j in range(3):
##        print((i,j))

##for i in [[1,2,3],'hello',(1,2,3)]:
##    print(i)
##    for j in i:
##        print(j)

##l=[1,2,[3,4,5,9],2,[6,2]]
##r=[]
##for i in l:
##    if isinstance(i,list):
##        for j in i:
##            r.append(j)
##    else:
##        r.append(i)
##print(r)

##for i in range(1,6):
##    for j in range(1,i+1):
##        print(j,end=' ')
##    print()

##for i in range(2,101):
##    flag=True
##    for j in range(2,i):
##        if i%j==0:
##            flag=False
##    if flag:
##        print(i)
#prime numbers between 1 to 100
##for i in range(2,101):
##    for j in range(2,i):
##        if (i%j)==0:
##            break
##    else:
##        print(i)

##l=[1,2,[3,[4,5],6,[7]]]
##r=[]
##for i in l:
##    if isinstance(i,list):
##        for j in i:
##            if isinstance(j,list):
##                for k in j:
##                    r.append(k)
##            else:
##                r.append(j)
##    else:
##        r.append(i)

#flatering a list
##l=[1,2,[3,4,5,[2,[3,4,],3,[2,3,4]],3,2],1,2]
##r=[]
##def flat(n):
##    for i in n:
##        if isinstance(i,list):
##            flat(i)
##        else:
##            r.append(i)
##flat(l)
##print(r)

#first n prime numbers
##n=int(input())
##i=1
##c=0
##while c<n:
##    flag=True
##    for j in range(2,i):
##        if i%j==0:
##            flag=False
##    if flag:
##        print(i)
##        c+=1
##    i+=1

##num=int(input())
##res=0
##for i in str(num):
##    fact=1
##    n=int(i)
##    for j in range(1,n+1):
##        fact*=j
##    res+=fact
##if num==res:
##    print('strongest number=',res)
##else:
##    print('Not strongest number')

##x=[[1,2,3],
##   [4,5,6],
##   [7,8,9]]
##y=[[1,6,8],
##   [1,2,4],
##   [2,4,8]]
##z=[]
##for i in range(len(x)):
##    z.append([])
##    for j in range(len(x[i])):
##        k=x[i][j]+y[i][j]
##        z[i].append(k)
##print(*z,sep='\n')

##x=[[1,2],
##   [3,4],
##   [5,6],
##   [6,7],
##   [8,9]]
##r=[]
##for i in range(len(x[0])):
##    r.append([])
##    for j in range(len(x)):
##        r[i].append(x[j][i])
##print(r)

##num=1
##c=1
##while c<10:
##    res=0
##    for i in str(num):
##        fact=1
##        n=int(i)
##        for j in range(1,n+1):
##            fact*=j
##        res+=fact
##    if num==res:
##        print(num)
##        c+=1
##    num+=1

##num=int(input())
##c=1
##n=1
##while c<num:
##    s=0
##    for i in range(1,n):
##        if n%i==0:
##            s+=i
##    if n==s:
##        print(n)
##        c+=1
##    n+=1

##l='''Nature is the essential, vibrant force encompassing all living and non-living things—from towering mountains to the smallest insects—that sustains life on Earth. It provides vital resources like clean air, water, and food while fostering biodiversity. Beyond physical survival, nature offers immense beauty, peace, and healing, acting as a crucial sanctuary for mental well-being. However, this interconnected ecosystem faces threats from human activity, including deforestation and pollution, making it our moral duty to protect and preserve it.'''
##d={}
##for i in l:
##    if i not in d:
##        d[i]=1
##    else:
##        d[i]+=1
##print(d)

##l='this'
##p=[]
##for i in range(len(l)):
##    for j in range(i+1,len(l)+1):
##        p.append(l[i:j])
##print(p)

##l=[9,4,3,5,1,2,8,6,0,7]
##n=len(l)
##for i in range(n):
##    for j in range(n-i-1):
##        if l[j]>l[j+1]:
##            l[j],l[j+1]=l[j+1],l[j]
##print(l)

##l=[1,2,3,4]
##p=[]
##for i in range(len(l)):
##    for j in range(i+1,len(l)):
##        p.append((l[i],l[j]))
##print(p)
        
##r=0
##for i in range(1,10):
##    r=r*10+i
##    print(r,end=' ')

l=[1,2,3,4,5,6,7,8,9,0]
d=set()
t=9
for i in l:
   for j in l:
       if ((i+j)==t and (i,j) not in d and (j,i) not in d):
           d.add((i,j))
print(d)

#prime factors of number
##l=[]
##n=int(input())
##for i in range(2,n+1):
##    if n%i==0:
##        for j in range(2,i):
##            if i%j==0:
##                break
##        else:
##            l.append(i)
##print(l)


##l=[]
##h=0
##n,m=map(int,input().split())
##for i in range(1,n+1):
##    if n%i==0 and m%i==0:
##        l.append(i)
##        if i>h:
##            h=i
##print(h)

##def lcm(a,b):
##    h=0
##    for i in range(2,b+1):
##        if a*i and b*i:
##            h=i
##            break
##    return h
##print(lcm(10,10))
