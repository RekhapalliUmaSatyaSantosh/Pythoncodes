##i=1
##while i<=100:
##    print(i,end=' ')
##    i+=1

##i=10
##while i>0:
##    print(i)
##    i-=1

##i=0
##while i<20:
##    if i%2==0:
##        print(i,end=' ')
##    i+=1

##i=0
##res=0
##n=int(input())
##while i<=n:
##    res+=i
##    i+=1
##print(res)

##n=int(input())
##i=1
##while i<=20:
##    print(n,'x',i,'=',n*i)
##    i+=1
    
##n=int(input())
##i=1
##while i<n:
##    i+=1
##print(i*(i+1))

##n=int(input())
##while n:
##    break
##if n%2==0:
##    print('Even number')

##n=int(input())
##i=2
##while i*i<=n:
##    if n%i==0:
##        print('Not a prime')
##        break
##    i+=1
##else:
##    print('Prime number')

##n=int(input())
##for i in range(2,int(n**0.5)+1):
##    if n%i==0:
##      print('Not a prime')
##else:
##    print('prime number')

##num=int(input())
##temp=num
##res=0
##while temp>0:
##    r=temp%10
##    res=(res*10)+r
##    temp//=10
##if temp==res:
##    print('Palindrome')
##else:
##    print('Not palindrome')

##num=int(input())
##i=0
##while num:
##    num//=10
##    i+=1
##print(i)

##n=int(input())
##while n>0:
##    n//=10
##    print(n)

##n=int(input())
##temp=n
##res=0
##count=0
##while temp>0:
##    count+=1
##    res+=(res**count)
##    temp//=10
##if temp==res:
##    print('armstrong')
##else:
##    print('Not armstrong')

##n=int(input())
##temp=n
##i=1
##res=0
##while i<temp:
##    if temp%i==0:
##        res+=i
##    i+=1
##if temp==res:
##    print('Strong number')
##else:
##    print('Not Strong number')

##n=input()
##l={}
##i=0
##while i<len(n):
##    ch=n[i]
##    if ch in l:
##        l[ch]+=1
##    else:
##        l[ch]=1
##    i+=1
##i=0
##while i<len(n):
##    if l[n[i]]==1:
##        print(n[i])
##        break
##    i+=1
##else:
##    print('No repeated character')

##n=int(input())
##i=2
##val=1
##while n>0:
##    val*=i
##    print(val)
##    n-=1

##n=int(input())
##if n&(n-1):
##    print('Not power of 2')
##else:
##    print('Power of 2')

##n=int(input())
##temp=n
##po2=True
##while temp !=1:
##    if temp%2==0:
##        temp//=2
##    else:
##        po2=False
##        temp=1
##if po2:
##    print("Power of 2")
##else:
##    print("Power of 2")

##n=input()
##d={}
##i=0
##while i<len(n):
##    if n[i] in d:
##        d[n[i]]+=1
##    else:
##        d[n[i]]=1
##    i+=1
##print(d)
##x=list(d.items())
##x.sort()
##print(x)
##h=x[-1][0]
##sh=x[-2][0]
##print(h,sh)
##h=''
##sh=''
##i=0
##while i<len(x):
##    if d.get(h,0)<x[i][1]:
##        sh=h
##        h=x[i][0]
##    elif d.get(sh,0)<x[i][1]<d[h]:
##        sh=x[i][0]
##    i+=1
##print(h,sh)

#frequency of each element in list
##n=eval(input())
##d={}
##i=0
##while i<len(n):
##    if n[i] in d:
##        d[n[i]]+=1
##    else:
##        d[n[i]]=1
##    i+=1
##print(d)
##print(list(d.items()))
#count of specific element in list
##l=eval(input())
##n=int(input())
##print(l.count(n))

##n=int(input())
##i=0
##j=1
##while n>0:
##    d=n%10
##    i+=d
##    j*=d
##    n//=10
##print(i,j)
##if i==j:
##    print('SPY number')
##else:
##    print('Not spy number')

#even characters of string
##n=input()
##i=0
##d=''
##while i<len(n):
##    d+=n[i]
##    i+=2
##print(d)

# n=int(input())
# res=1
# while n:
#     res*=n
#     n-=1
# print(res)

# n=input()
# vowels='aeiouAEIOU'
# i=0
# c=0
# while i<len(n):
#     if n[i] in vowels:
#         c+=1
#     i+=1
# print(c)

# n=int(input())
# num=3
# r=0
# for i in range(1,n+1):
#     r+=num*i
# print(r)

def circle_perimeter(r):
    result=2*3.14*r
    return result
print(circle_perimeter(100))
