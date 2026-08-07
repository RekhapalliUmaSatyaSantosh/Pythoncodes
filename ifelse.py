##a=int(input())
##if a>0:
##    print('+ve')
##else:
##    print('-ve')

##a=eval(input())
##if type(a) in [tuple,int,float,str,complex]:
##    print('immutable')
##else:
##    print('mutable')

##a=eval(input())
##if isinstance(a,int):
##    print('integer')
##else:
##    print('Not integer')

##a=input()
##if 'A' <= a <= 'Z' or 'a'<=a<='z' or '1'<=a<='9':
##    print('not special')
##else:
##    print('special')

##a=int(input())
##b=str(a)
##if b==b[::-1]:
##    print('Palindrome')
##else:
##    print('Not palindrome')

##a=eval(input())
##if len(a)%2==0:
##    print('no middle value')
##else:
##    print('middle val is=',a[len(a)//2])

##for i in range(ord('A'),ord('z')+1):
##    print(chr(i),end=' ')
##    i+=1

##a=int(input())
##if a%5==0:
##    print('Divisible by 5')
##else:
##    print('Not divisible by 5')

##age=int(input())
##if age>=18:
##    print('Major')
##else:
##    print('Minor')

##a=input()
##if a.isupper():
##    print('True')
##else:
##    print('False')

##a=int(input())
##if a>50:
##    print('Greater than 50')
##else:
##    print('Less than 50')

##a=input()
##if a in ['A','E','I','O','U','a','e','i','o','u']:
##    print('Vowel')
##else:
##    print('Consonent')

##marks=int(input())
##if marks>=40:
##    print('Passed')
##else:
##    print('Failed')

##a,b=map(int,input().split())
##if a>b:
##    print('A is greater than B')
##else:
##    print('B is greater than A')

##a=int(input())
##if 10<=a<=50 and a!=25:
##    print('10 to 50 without 25')
##else:
##    print('10 to 50')

##a=int(input('Enter your age='))
##b=int(input('Enter you amount='))
##if (a<18 or a>60) and b>500:
##    print('Eligible for discount')
##else:
##    print('Not Eligible for discount')

##a=int(input())
##if a%2!=0 or a in [6,8,10,12,14,16,18,20]:
##    print('Weired')
##else:
##    print('Not weired')

##a=int(input())
##if a%4==0 and a%100!=0 or a%400==0:
##    print('leap year')
##else:
##    print('Not leap year')

##a=input()
##b=input()
##if a.lower()==b.lower():
##    print('Equal')
##else:
##    print('Not Equal')

##n=int(input())
##if n>0:
##    m=n//2
##    res=m*(m+1)
##    print('The result=',res)
##else:
##    print('Not positive number')

##a=int(input())
##if a%2==0 or a%3==0:
##    print('Divisible by 2 or 3')
##elif a%2==0 and a%3==0:
##    print('Divisible by 2 and 3')
##else:
##    print('Not divisible')

##a=input().lower()
##if ('a'in a) or ('e' in a) or ('i' in a) or ('o' in a) or ('u' in a):
##    print('Contians vowel')
##else:
##    print('Not contians vowel')

# a,b,c=map(int,input().split())
# if a+b<=c or b+c<=a or a+c<=b:
#    print('Not a Triangle')
# elif a==b and b==c:
#    print('Equilateral')
# elif a==b or b==c or c==a:
#    print('Isosceles')
# else:
#    print('Scalane')

#list is empty or not
##a=list(map(int,input().split()))
##if len(a)==0:
##    print('Empty list')
##else:
##    print('Non empty list')

#contains only digits
##a=input()
##if a.isdigit():
##    print('Contains only digits')
##else:
##    print('Contains with digits')

#factor of another num
num=int(input())
if 