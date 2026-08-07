##n=5
##for i in range (n):
##    for j in range (n):
##        if(i<=0 or i<=n or j<=0 or j<=n):
##            print('*',end=' ')
##        else:
##            print(" ",end=' ')
##    print(" ")

##n=5
##for i in range (n+1):
##    for j in range(n+1):
##        if(i==0 or i==n or j==0 or j==n):
##            print('*',end=' ')
##        else:
##            print(" ",end=' ')
##    print(" ")

##for i in range(5,1,-1):
##    for j in range(1,i):
##        print('*',end=' ')
##    print()
##
##for i in range(1,6):
##    for j in range(i,5):
##        print(' ',end=' ')
##    for j in range(i,0,-1):
##        print('*',end=' ')
##    print()

##n=5
##for i in range(n,1,-1):
##    for j in range(n-i):
##        print('  ',end=' ')
##    for j in range(i):
##        print('*',end=' ')
##    print()

##n=5
##for i in range(1,n):
##    print(' '*(n-i),end='')
##    print('* '*i)
##for i in range(n,0,-1):
##    print(' '*(n-i),end='')
##    print('* '*i)

##n=4
##for i in range(1,n+1):
##    print(f'{'* '*i:^10} ')

##n=1
##for i in range(1,int(input())):
##    for j in range(i):
##        print(n,end=' ')
##        n+=1
##    print()

##for i in range(1,6):
##    for j in range(i):
##        if (i+j)%2==0:
##            print('0',end=' ')
##        else:
##            print('1',end=' ')
##    print()

##n=5
##for i in range(n+1):
##    for j in range(n-i):
##        print('',end=' ')
##    for j in range(i):
##        print(i,end=' ')
##    print()

##n=6
##for i in range(n):
##    for j in range(n-i-1):
##        print('',end=' ')
##    val=1
##    for j in range(i+1):
##        print(val,end=' ')
##        val=val*(i-j)//(1+j)
##    print()
    
##n = 8
##for i in range(n):
##    for j in range(n):
##        if (i+j) % 2 == 0:
##            print("⬜", end="")
##        else:
##            print("⬛", end="")
##    print()

n=5
for i in range(n+1):
    for j in range(n-i):
        print(' ',end='' )
    for j in range(i):
        print(j+1,end=' ')
    print()
