##x=[[1,2,3],
##   [4,5,6],
##   [7,8,9]]
##y=[[1,2,3],
##   [4,5],
##   [7,8,9]]
##r=[]
##for i in range(len(x)):
##    r.append([])
##    if len(x[i])==len(y[i]):
##        for j in range(len(x[i])):
##            k=x[i][j]+y[i][j]
##            r[i].append(k)
##    else:
##        print('Not equal')
##        del r
##        break

##n=eval(input())
##d={}
##if isinstance(n,(list,tuple,set,dict)):
##    for i in n:
##        if i not in d:
##            d[i]=1
##        else:
##            d[i]+=1
##else:
##    for i in str(n):
##        if i not in d:
##            d[i]=1
##        else:
##            d[i]+=1
##print(d)

##def bin(n):
##    r=''
##    while n:
##        r+=str(n%2)
##        n//=2
##    return r[::-1]
##print(bin(10))

##a=[[-1,-2,-3],[-14,-5,-6],[-100,-10,-3],[-7,-8,-9],[-14,-5,-6],[0,0,0]]
##print(max(a))

x=[[1,2,3],
   [4,5,6]]
y=[[1,2,3],
   [4,5,6]]
def mat(a,b):
    z=[]
    for i in range(len(a)):
        z.append([])
        if a[i]==b[i]:
            for j in range(len(a[i])):
                z[i].append(a[i][j]+b[i][j])
        else:
            return 'Not Equal'
            del z
            break
    return z
r=mat(x,y)
print(r)









































