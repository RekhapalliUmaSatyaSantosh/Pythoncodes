# print("hello world")

# num=int(input("Enter a number: "))
# fact = 1
# if num ==0 or num==1:
#     print(num)
# else:
#     for i in range(2,num+1):
#         fact*=i
#     print(fact)

# p1=str(input())
# p2=str(input())
# if(p1==p2):
#     print('Match tied')
# elif(p1=='rock' and p2=='paper' or p2=='scissor'):
#     print('player 1 wins')
# elif(p1=='scissor' and p2=='paper'):
#     print('player 1 wins')
# elif(p2=='scissor' and p1=='paper'):
#     print('player 2 wins')
# elif(p2=='rock' and p2=='paper' or p2=='scissor'):
#     print('player 2 wins')

# n=int(input())
# c=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(c,end=" ")
#         c=c+1
#     print("\n")
# print('='*20)
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print("\n")
# print('='*20,end=" ")

# print(' (._.)')
# print('<(   )>')
# print(' (_^_)')

# y=int(input())
# if y%400==0:
#     print('Yes! It is a leap year')
# elif y%100==0:
#     print('No! It is not a leap year')
# elif y%4==0:
#     print('Yes! It is a leap year')
# else:
#     print('No! It is not a leap year')

# f=float(input())
# i=int(f*100)
# print(i)

# i=int(input())
# num=-i
# print(num)

# p1={'i','n','d','i','a'}
# p2={'c','h','i','n','a'}
# p3=p1.intersection(p2)
# print(len(p3))

# i=str(input())
# if '_' in i:
#     i=i.split('_',1)
#     print(i)
# else:
#     print(i[::-1])

# n=int(input())
# m=int(input())
# a=input()
# if(a=='a'):
#     a=n+m
# elif(a=='s'):
#     a=n-m
# elif(a=='m'):
#     a=n*m
# elif(a=='d'):
#     a=n//m
# print(a)

# for num in range(1,6):
#     print(num,'-',num*num)

# for i in range(1,5):
#     print('****')

# matrix=[[7,2,3,6],
#         [4,5,6,7],
#         [1
#          ,8,9,4]]
# m,n=len(matrix),len(matrix[0])
# left,right=0,n-1
# top,bottom=0,m-1
# result=[]
# while top <= bottom and left <= right:
#         for i in range(left, right + 1):
#             result.append(matrix[top][i])
#         top += 1
#         for i in range(top, bottom + 1):
#             result.append(matrix[i][right])
#         right -= 1
#         if top <= bottom:
#             for i in range(right, left - 1, -1):
#                 result.append(matrix[bottom][i])
#             bottom -= 1
#         if left <= right:
#             for i in range(bottom, top - 1, -1):
#                 result.append(matrix[i][left])
#             left += 1  
# print(" ".join(map(str, result)))

# a,b=map(int,input().split())
# c=a+b+(a*b)
# print(c)

# n=int(input())
# if n%2!=0:
#     print("Weird")
# elif n%2==0 and 2 <= n <= 5:
#     print("Not Weird")
# elif n%2==0 and 6 <= n <= 20:
#     print("Weird")
# elif n%2==0 and n > 20:
#     print("Not Weird")

# f=float(input())
# i=f*100
# print(int(i))

# n=int(input())
# if n==n:
#     m=-n
#     print(m)
# elif n==-n:
#     print(n)

# s1=set(input())
# s2=set(input())
# s=s1.intersection(s2)
# print(len(s))

s=input()
n=s.index('_')
if n==-1:
    print(s[::-1])
elif n==len(s)-1:
    print(s[:len(s)-1]+'_')
else:
    print(s[:n][::-1]+s[n:])