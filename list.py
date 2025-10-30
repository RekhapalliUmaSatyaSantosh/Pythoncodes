# fruits_1=["apple","banana","cherry"]
# fruits_2=["orange","kiwi","mango"]
# fruits_1.extend(fruits_2)
# print(fruits_1)

# list=['ZERo','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
# num = int(input("Enter a number between 0 to 9:"))
# print(list[num])

# list1 = [1,2,3,4,5]
# list1.remove()
# print(list1)

# a = [1, 2, 3, None, [1, 2, 3, 4, 5],['Geeks', 'for', 'Geeks']] 
# print(len(a))

# num=int(input("Enter a range:"))
# list=list(range(2,num+1,2))
# print(list)

# list=[]
# list.append(10)
# list.append('hello')
# list.append('bye')
# print(list)

# list='This is very good place to feel the soul'
# print(list.split())

# list=[10,283,49,23,821,8646,399,8837,388]
# m=sorted(list)
# print(m)

# list1=['hello','ball','apple']
# # m=sorted(list1)
# print(len(list1))

# l=eval(input("Enter elements:"))
# print(type(l))
# print(l)

# l=[0,1,2,3,4,5,6,7,8,9]
# # for x in l:
# #     if x%2==0:
# #         print(x)
# # i=0
# # while i<len(l):
# #     print('the element present at +ve index;{} and index:{} is:{}'.format(i,i-len(l),l[i]))
# #     i=i+1

# l1=l+[10,20]
# print(l1)

# l=[10,20,10,20,20,30,30,30,40,40,40]
# x=int(input("Enter element to remove:"))
# while True:
#     if x in l:
#         l.remove(x)
#     else:
#         break
# print('After removal',l)

# l=[10,20,30,40,50]
# l.clear(10)
# print(l)

# l=[[10,20,30],[40,50,60],[70,80,90]]
# l1
# print(l)
# for i in l:
#     for y in i:
#         print(y,end=' ')
#     print()
# l1=[[10,20,30],[40,50,60],[70,80,90]]
# print(l,l1)
# l.extend(l1)
# for i in l:
#     for j in i:
#         print(j,end=' ')
#     print()

# l=[10,20,30,40]
# l2=[30,40,50,60]
# l1=[x for x in l if x not in l2]
# print(l1)

# l=['Arya','Bhanu','Chaitu','Dan']
# l1=[x[0] for x in l ]
# print(l1)

# l='the quick brown fox jump over the lazy dog'
# words=l.split()
# print(words)
# l1=[x.upper()for x in words]
# print(l1)

# vowels=['a','e','i','o','u']
# word=input("Enter any word:")
# result=[ch for ch in vowels if ch in word]
# # for ch in word:
# #     if ch in vowels:
# #         result.append(ch)
# print(result)
# print("the unique vowels are:",len(result))

# x=[[10,20,30],
#    [40,50,60],
#    [70,80,90]]
# y=[[10,20,30],
#    [40,50,60],
#    [70,80,90]]
# result=[[0,0,0],
#         [0,0,0],
#         [0,0,0]]
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[i][j]=x[i][j]*y[i][j]
# for r in result:
#     print(r)

# l=eval(str(input()))
# num=int(input())
# list=[x for x in l for _ in range(num)]
# print(list)

# a=[122,742,425,98,37]
# a.sort(reverse=True)
# print(a[1])

# l=input()
# l1=input()
# l2=l+l1
# print(l2)

# n=int(input())
# if 1 <= n <=2000:
#     print(25)
# elif 2001 <= n <=4000:
#     print(35)
# elif 4001 <= n <=7000:
#     print(45)
# elif n>7000:
#     print('Overload')
# elif n==0:
#     print(0)
# elif n<0:
#     print('Invalid Input')

# x=int(input())
# y=int(input())
# for i in range (x+1,y):
#     if i %2!=0:
#         print(i,end=' ')

# s=input()
# print(s[::-1])

# s=input()
# print(s[1:-1:1])

n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='')
    print()