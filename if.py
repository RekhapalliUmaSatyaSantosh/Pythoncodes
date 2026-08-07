##a=int(input())
##if a%2==0:
##    print(a**2)

##a=input()
##if a in ['A','E','I','O','U','a','e','i','o','u']:
##    print('vowel')

##a=input()
##if a.isupper():
##    print('upper and ascii val=',ord(a))

##a=int(input())
##if a%9==0 or a%6==0:
##    print(a**3)

##a=int(input())
##if len(str(a))==3:
##    print('3-digit number')


##a=int(input())
##if a%10==5:
##    print('Last digit is 5')

##a=eval(input())
##if isinstance(a,float):
##    print('float')

##a=eval(input())
##if isinstance(a,(int,float,complex,bool)):
##    print('Single valued data')

##a=input()
##if '0'<=a<='9':
##    print('digit')

##a=int(input())
##if a%3==0:
##    print('Multiple of 3')


##waptp square of a number only if it is even

##x=int(input("enter a number:"))
##if x%2==0:
##    print("square of the number is :",x**2)
##else:
##    print("not an even number")
    
##wapt check whether the character is vowel or not

##x=input("enter a character:")
##if len(x)==1 and x in 'AEIOUaeiou':
##    print("vowel")
##else:
##    print("not a vowel")

##wapt print ascii value of a character only if it is uppercase

##x=input("enter a character:")
##if x == x.upper() and x not in '1234567890':
##    print(ord(x))
##else:
##    print("character is in lower case or the value in number")
##

##wapt print cube of a number only if it is divisible by 9 or 6

##num=eval(input("enter a number:"))
##if num%9==0 or num%6==0:
##    print(f"cube of {num} is:{num**3}")
##else:
##    print("not divisible by 6 or 9")

##wapt check whether the given integer is 3 digit number or not

##a=eval(input("enter a number:"))
##if len(str(a))==3:
##    print("3 digit number")
##else:
##    print("not a 3 digit number")

##wapt check whether the last digit of a number is 5

##num=str(input("enter a number:"))
##if num%10==5:
##    print("last digit is 5")
##else:
##    print("last digit is not 5")

##wapt check wheter the given data is float

##x=eval(input("enter a num:"))
##if type(x)==float:
##    print("data is float")
##else:
##    print("not a float")

##wapt check whether the data is single value data

##x=eval(input("enter the data"))
##if type(x) in [bool,int,float,complex]:
##    print("single valued data")
##else:
##    print("not a single value")

##wapt check whether the given character is digit or not

##x=input("enter a character:")
##if len(x)==1 and '0'<=x<='9':
##    print("it is a digit")
##else:
##    print("not a digit")

##wapt check whether the given integer is multiple of 3

##x=eval(input("enter a number"))
##if x%3:
##    print("not divisible by 3")
##else:
##    print("multiple by 3")

##wapt check whether the data is mutuble or not

##x=eval(input("enter a data:-"))
##if type(x) in [list,set,dict]:
##    print("mutable")
##else:
##    print("immutable")

##wapt check whether the given character is special or not

##inp=str(input("enter a character:-"))
##if 'a'<=inp<='z' or 'A'<=inp<='Z' or '0'<=inp<='9':
##    print("not a special character")
##else:
##    print("special character")

##wapt check whether a list consist of middle value or not

##x=eval(input("enter a list:"))
##if len(x)%2==0:
##    print("have nomiddle value")
##else:
##    print("have middle value",x[len(x)//2])

##wapt check whether two values are pointing to same mamory or not 

##x=input("enter a value:")
##y=x
##if id(x)==id(y):
##    print("both are showing same address")
##else:
##    print("diff address")

#uppercase or not
##a=input()
##if a in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
##    print('Character in upper case')

#if string contains a
##a=input()
##if 'a' in a or 'A' in a:
##    print('A in string')

#list has >5 elements
##a=list(map(int,input().split()))
##if len(a)>5:
##    print('The list has more than 5 elements')

#list has +ve elements
##a=list(map(int,input().split()))
##for i in a:
##    if i>0:
##        print(i,'is a Positive element')
##    else:
##        print(i,'is a Negative element')

#perfect square or not
##a=int(input())
##r=(a**0.5)
##if r*r==a:
##    print('Perfect square')

#empty string or not
##a=input()
##if a=='':
##    print('Empty string')


