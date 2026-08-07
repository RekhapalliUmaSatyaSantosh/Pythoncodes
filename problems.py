##temp=int(input('Enter Temperature='))
##c=input('convert into (C/F)=')
##if c.lower()=='c':
##    print('The temperature in celsisus=',(temp-32)*(5/9))
##elif c.lower()=='f':
##     print('The temperature in fahrenheit=',(temp*1.8)+32)
##else:
##    print('Please enter a valid input')

##inp=int(input())
##r=0
##for i in str(inp):
##    r+=int(i)
##print(r)

##for i in range(1,6):
##    for j in range(1,i+1):
##        print('*',end=' ')
##    print()



##l=[1,2,3,4,5,6,7,8,9,10]
##d={'even':[],'odd':[]}
##for i in l:
##    if i%2==0:
##        d['even'].append(i)
##    else:
##
##        d['odd'].append(i)
##print(d)

##n=input()
##m=n.replace(' ','').lower()
##r=''
##for i in m:
##    r=i+r
##if r==m:
##    print('Palindrome')
##else:
##    print('Not Palindrome')

##n=int(input())
##original=n
##c=0
##r=0
##while n>0:
##    res=n%10
##    r+=res
##    c+=1
##    n//=10
##if original%2==0:
##    print(("Even",c,r))
##else:
##    print(("Odd",c,r))

##def isprime(n):
##    for i in range(2,int(n**0.5)+1):
##        if n%i==0:
##            return False
##    return True
##print(isprime(23))
##def find_primes_in_range(start, end):
##    l=[]
##    if start>end:
##        start,end=end,start
##    for i in range(start,end+1):
##        if isprime(i):
##            l.append(i)
##    return l
##  
##print(find_primes_in_range(20,10))

##l1 = [1, 2, 3, 4, 5, 6, 7]
##l2 = [2, 3, 4, 8, 9]
##def similar(a, b):
##    r = []
##    for i in a:
##        if i in b and i not in r:
##            r.append(i)
##    r.sort()
##    return r
##print(similar(l1, l2))
##def operations(a):
##    if not a:
##        return {"sum": 0, "average": 0, "max": None, "min": None, "unique_count": 0}
##    total = 0
##    max_val = a[0]
##    min_val = a[0]
##    unique = []
##    for i in a:
##        total += i
##        if i > max_val:
##            max_val = i
##        if i < min_val:
##            min_val = i
##        if i not in unique:
##            unique.append(i)
##    avg = total / len(a)
##    unique_count = len(unique)
##    return {"sum": total, "average": avg, "max": max_val, "min": min_val, "unique_count": unique_count}
##print(operations(l1))

# def fib():
#     a,b=0,1
#     for _ in range(1,11):
#         print(a,end=' ')
#         a,b=b,a+b
# fib()

# a='Today is Friday'
# print(a.split()[::-1])

# a='tiger'
# l=len(a)
# for i in range(l):
#     for j in range(l):
#         if i==l//2 and j==l//2:
#             print(a[j],end='')
#         elif i!=l//2 and (j==0 or j==l-1):
#             print(a[j],end='')
#         else:
#             print(' ',end='')
#     print()

# a='In 1885 it was banished from the shelves of the Concord Public Library, an act that attracted a lot of publicity and discussion in the press. It is still frequently in the news, as various schools and school systems across the country either ban it from or restore it to their classrooms. The texts and illustrations below attempt to capture both the novels achievement and some aspects of its controversiality.'
# b=a.lower().split()
# c=0
# for i in b:
#     if i in ('a','an','the'):
#         c+=1
# print(c)

# def unique(s):
#     b={}
#     for i in s:
#         if i in b:
#             b[i]+=1
#         else:
#             b[i]=1
#     for i,j in enumerate(s):
#         if b[j]==1:
#             return i
#     return -1
# print(unique('aabbcdeed'))   

# def target(l,t):
#      for i in range(len(l)):
#          for j in range(i+1,len(l)):
#              if l[i]+l[j]==t:
#                 return [i,j]
# print(target([1,2,3,4,5,6,7,8,9,0],9))

# def factorial(n):
#     if n<=1:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(5))  
# print(factorial(0))
# print(factorial(3))

# def missing(l):
#     l.sort()
#     for i in range(len(l)+1):
#         if i not in l:
#             return i
# print(missing([0,4,2,1,5,6,7,3]))

# def missing(l):
#     l.sort()
#     m=[]
#     for i in range(min(l),max(l)+1):
#         if i not in l:
#             m.append(i)
#     return m
# print(missing([1,0,4,2,7,9,5]))
    
# a=[1,2,3,4,5,6,7]
# r=[]
# for i in a:
#     if i%2==0:
#         r.append(i*i)
# print(r)

# def char_freq(n):
#     r={}
#     for i in n:
#         if i not in r:
#             r[i]=1
#         else:
#             r[i]+=1
#     return r
# print(char_freq('hellohowareyouithinkyouareveryfine'))

# def remove_dup(n):
#     r=[]
#     for i in n:
#         if i not in r:
#             r.append(i)
#     return r
# print(remove_dup('heloloe'))
# print(remove_dup([1,2,3,4,5,6,5,4,3,2,1]))

# def missing_num(n):
#     l=len(n)
#     for i in range(l+1):
#         if i not in n:
#             return i
# print(missing_num([0,1,2,3,4,6,7,8,9]))

# def anagrams(a,b):
#     s1=a.replace(" ","").lower()
#     s2=b.replace(" ","").lower()
#     return sorted(s1)==sorted(s2)
# print(anagrams("Light","Thigl"))

# def fizzbuzz(n):
#     r=[]
#     for i in range(1,n+1):
#         if (i%3==0 and i%5==0):
#             r.append('FizzBuzz')
#         elif i%3==0:
#             r.append('Fizz')
#         elif i%5==0:
#             r.append('Buzz')
#         else:
#             r.append(i)
#     return r
# print(fizzbuzz(15))

# def palindrome(n):
#     temp=''.join(i for i in n if i.isalnum()).lower()
#     r=''
#     for i in temp:
#         r=i+r
#     if r==temp:
#         return True
#     else:
#         return False
# print(palindrome('A man, a plan, a canal: Panama'))

# def dupliacate(n):
#     r=[]
#     for i in n:
#         r.append(i)
#         if i in r:
#             return i
#     return r
# print(dupliacate([1,2,3,4,1,2]))

# a=[]
# n=int(input('How much size do you want='))
# for i in range(1,n+1):
#     val=int(input(f'Enter {i} value='))
#     a.append(val)
# print(a)

# l=[1,2,34,5,6,72,68,7,8,9,8,66,7,76]    
# a=[x for x in l if x%2==0]
# print(a)

# l=[1,2,3,3,4,5,67,7,5,8]
# print(sum(l)/len(l))

# l=[1,2,3,4,5,6,7,8,9,10]
# r=0
# for i in range(len(l)):
#     if i%2:
#         r+=l[i]
# print(r)

# l=[1,3,45,6,7,8,9,6]
# # p=len(l)//2
# # m=l[:p]
# r=[]
# for i in range(len(l)):
#     if i%2:
#         r.append(l[i])
# print(sum(r)/len(r))
# print(r)

# l=[1,2,4,5,678,908,0,7,5,442,45,67,8,9,3,123]
# print(max(l))
# h=0
# s=0
# for i in l:
#     if i>h:
#         h=i
#     if i<s:
#         s=h
# print(h,s)

# l=[1,2,4,5,678,908,0,7,5,442,45,67,8,9,3,123]   #sorting an list
# n=len(l)
# for i in range(n):
#     for j in range(0,n-i-1):
#         if l[j]<l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)

# l=[1,2,3,21,3,2,5,4,4,1,3,33]
# n=4
# for i in range(len(l)):
#     if l[i]==n:
#         print('Element is their at index=',i)
#         break

# def unique(s):
#     d={}
#     for i in s:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     for i,j in enumerate(s):
#         if d[j]==1:
#             return i
#     return -1
# print(unique('abbcedsa'))

# def process_data(data):
#     if isinstance(data,list):
#         r=0
#         for i in data:
#             r+=i
#         return r
#     elif isinstance(data,dict):
#         r={k:v*v for k,v in data.items()}
#         return r
#     elif isinstance(data,str):
#         r=' '
#         for i in data:
#             r=i+r
#         return r
#     elif isinstance(data,(int,float)):
#         return data*data
#     else:
#         raise TypeError
# print(process_data([1,2,3]))
# print(process_data({'a':2,'b':3}))
# print(process_data('santosh'))
# print(process_data(12))
# print(process_data(12.4))
# print(process_data((1,2,3)))

# l=['apple','baggs','appla','santu','santo','kings','satyb','satya']
# for i in range(len(l)):
#     for j in range(len(l)-1):
#         if len(l[j])>len(l[j+1]):
#             l[j],l[j+1]=l[j+1],l[j]
#         elif len(l[j])==len(l[j+1]):
#             if l[j]>l[j+1]:
#                 l[j],l[j+1]=l[j+1],l[j]
# print(l)

# l=[9,4,2,6,1,8,1,0,3,5,7]
# for i in range(len(l)):
#     for j in range(len(l)-1):
#         if l[j]>=l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)

# class Savage:
#     name='Hero1'
#     def __init__(self,name):
#         self.name=name
    # def display(self):
    #     a=10
    #     if 'a' in locals():
    #         print("Yes, 'my_var' is a local variable.")
    #     else:
    #         print("No, it is not local.")
    # @classmethod
    # def display(cls):
    #     print(id(cls))
# s=Savage('Hero')
# print(id(s))
# s.display()
# print(Savage.name)
# print(Savage.__dict__)

# class test:
#     def __init__(self):
#         self.a1=10
#         self.b=20
#     def m1(self):
#         self.c=10
#         del self.b
# t=test()
# print(t.__dict__)
# t.m1()
# print(t.__dict__)
# t.d=40
# print(t.__dict__)
# del t.d,t.c,t.a1
# print(t.__dict__)

# class test:
#     e=132
#     print(e)
#     def __init__(self):
#         self.a=10
#         self.b=20
#         test.e=230
#     def m1(self):
#         print(self.a,self.b,test.e)
#         self.a=11
#         self.b=12
#         print(self.a,self.b)
#     @classmethod
#     def m2(cls):
#         cls.e=443
#         print(cls.e)
#         test.e=445
#         print(test.e)
# t=test()
# t.m1()
# print(t.__dict__)
# t.a=21
# t.b=22
# print(t.__dict__)
# t.m2()


# for i in range(0,1000):
#     if i%7==0:
#         d=str(i)
#         r=0
#         for j in d:
#             r+=int(j)
#         if r%3==0:
#             print(i)

# from datetime import datetime 
# now=datetime.now()
# print('Today is ',now.strftime('%Y-%m-%d'),' and it is ',now.strftime('%H:%M:%S'))

# def missing_card(cards):
#     colors = {"S", "H", "D", "C"}
#     values = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}
#     all_cards = {color + value for color in colors for value in values}
#     given_cards=set(cards.split())
#     missing=all_cards-given_cards
#     return missing.pop()

# def from_roman_numeral(roman_numeral):
#     roman_values = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }
#     t=0
#     pv=0 
#     for i in reversed(roman_numeral):
#         cv=roman_values[i]
#         if cv<pv:
#             t-=cv
#         else:
#             t+=cv
#         pv=cv
#     return t

# from datetime import datetime,timedelta,date
# def friday_the_13th():
#     today=datetime.now().date()
#     check_date = today
#     while True:
#         if check_date.day == 13 and check_date.weekday() == 4:
#             return check_date.strftime("%Y-%m-%d")
#         check_date += timedelta(days=1)

# def how_to_pay(amount,currency):
#     ind=[1,2,5,10,20,50,100,200,500]
#     d={}
#     de=sorted(ind,reverse=True)
#     r=amount
#     for i in de:
#         if r>=i:
#             count=r//i
#             d[i]=count
#             r-=count*i
#     return d
# print(how_to_pay(683,"ind"))

# def love(bob,alice):
#     return set(bob)&set(alice)
# def affair_meet(bob, alice, silvester):
#     b=set(bob)
#     a=set(alice)
#     s=set(silvester)
#     sa=a&s
#     safe=sa-b
#     return safe
# print(love(['Ⅱ', 'Ⅳ', 'ⅩⅠⅩ', 'ⅩⅤ', 'Ⅳ', 'Ⅱ'],['Ⅳ', 'Ⅲ', 'Ⅱ', 'ⅩⅩ', 'Ⅱ', 'ⅩⅩ']))
# print(affair_meet(['Ⅱ', 'Ⅳ', 'Ⅱ', 'ⅩⅠⅩ', 'ⅩⅤ', 'Ⅳ', 'Ⅲ'],['Ⅳ', 'Ⅲ', 'Ⅱ', 'XX', 'Ⅱ', 'ⅩⅩ'],['ⅩVⅢ', 'ⅩⅠⅩ', 'Ⅲ', 'Ⅰ', 'Ⅲ', 'ⅩVⅢ']))

# def decks(deck):
#     mid=len(deck)//2
#     first=deck[:mid]
#     second=deck[mid:]
#     res=[]
#     for i in range(mid):
#         res.append(first[i])
#         res.append(second[i])
#     return res
# print(decks([1,2,3,4,5,6]))

# r=[]
# def flatten(a_list):
#     for i in a_list:
#         if isinstance(i,list):
#             flatten(i)
#         else:
#             r.append(i)
#     return r
# print(flatten([1]))
# print(flatten([1]))

# num=12
# power=num*num
# res=0
# while num:
#     n=num%10
#     res=n+(res*10)
#     num//=10
# pow2=res*res
# temp=pow2
# rev=0
# while temp:
#     m=temp%10
#     rev=m+(rev*10)
#     temp//=10
# pow2=res*res
# if power==rev:
#     print('adam number')
# else:
#     print('not adam number')

# def adam_number(num):
#     power=num*num
#     res=''
#     for i in str(num):
#         res=i+res
#     r=int(res)
#     pow2=r*r
#     rev=''
#     for i in str(pow2):
#         rev=i+rev
#     re=int(rev)
#     if re==power:
#         return 'adam number'
#     else:
#         return 'not adam number'
# print(adam_number(995))

# def draw_n_squares(n):
#     result = ""

#     border = "+---" * n + "+\n"
#     middle = "|   " * n + "|\n"

#     for i in range(n):
#         result += border
#         result += middle

#     result += border

#     return result.rstrip()
# print(draw_n_squares(5))

# import unicodedata

# for i in range(0x110000): 
#     try:
#         ch = chr(i)
#         if "HEART" in unicodedata.name(ch):
#             print(ch, end=" ")
#     except ValueError:
#         pass

# with open('word.txt','r') as f:
#     f1=f.read()
#     c=0
#     for i in f1:
#         if i=='e':
#             c+=1
#     print(c)

# def caesar_cypher_encrypt(s, key):
#     res=''
#     for i in s:
#         if i.isalpha():
#             if i.isupper():
#                 res += chr((ord(i) - ord('A') + key) % 26 + ord('A'))
#             else:
#                 res += chr((ord(i) - ord('a') + key) % 26 + ord('a'))
#         else:
#             res+=i
#     return res

# def caesar_cypher_decrypt(s, key):
#     r=''
#     for i in s:
#         if i.isalpha():
#             if i.isupper():
#                 r+=chr((ord(i)-ord('A')-key)%26+ord('A'))
#             else:
#                 r+=chr((ord(i)-ord('a')-key)%26+ord('a'))
#         else:
#             r+=i
#     return r

# def list_pretty_print(items):
#     for i in range(0,len(items),5):
#         print(*items[i:i+5],sep=", ")
# list_pretty_print([1,2,3,4,5,6,7,8,9])

# n='hello'
# m='hi'
# print(n[1::-1])

# num=14
# count=0
# while num != 0:
#     if num % 2 == 0:
#         num //= 2
#     else:
#         num -= 1
#     count += 1
# print(num,count)

# nums=[11,7,4]
# print(nums[0]+nums[1])

# def duplicates(num):
#     res=[]
#     for i in num:
#         if num.count(i)==1:
#             res.append(i)
#     return res
# print(duplicates([1,2,3,1,1,4]))

# n='the'
# for i in n:
#     print(i*2,end='')

# nums=[1,2,3,4,100]
# h=max(nums)
# l=min(nums)
# nums.remove(h)
# nums.remove(l)
# n=sum(nums)//len(nums)

# def second_largest(num):
#     sh=-1
#     h=-1
#     for i in num:
#         if i>h:
#             sh=h
#             h=i
#         elif sh<i<h and h!=0:
#             sh=i
#     return sh
# print(second_largest([10, 5, 8,9, 10, 3]))


# def first_non_repeating(s):
#     for i in s:
#         if s.count(i)==1:
#             return i
#     return None
# print(first_non_repeating('swiss'))

# def longest(l):
#     c=1
#     maxx=1
#     for i in range(len(l)):
#         for j in range(len(l)-1):
#             if l[j]>=l[j+1]:
#                 l[j],l[j+1]=l[j+1],l[j]
#     for i in range(len(l)-1):
#         if l[i+1]==l[i]:
#             continue
#         elif l[i+1]==l[i]+1:
#             c+=1
#         else:
#             maxx=max(maxx,c)
#             c=1
#     return max(maxx,c)
# print(longest([1,4,3,17,2,90]))

# def product_except_self(l):
#     res=[]
#     for i in range(len(l)):
#         r=1
#         for j in range(len(l)):
#             if i!=j:
#                 r*=l[j]
#         res.append(r)
#     return res
# print(product_except_self([1,2,3,4]))

# def move_zeroes(nums):
#     t=0
#     r=0
#     for i in nums:
#         if i!=t:
#             nums[r]=i
#             r+=1
#     for i in range(r,len(nums)):
#         nums[i]=t
#     return nums
# print(move_zeroes([0,2,5,0,5,2,0]))

# def missing_number(nums):
#     h=nums[0]
#     for i in nums:
#         if i>h:
#             h=i
#     for i in range(h+1):
#         if i not in nums:
#             return i
# print(missing_number([0,1,3,4]))

# def sum(nums,t):
#     d=set()
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if (nums[i]+nums[j])==t and (nums[i],nums[j]) not in nums and (nums[j],nums[i]) not in d:
#                 d.add((i,j))
#     return d
# print(sum([1,2,4,3,5,6,7,8,9,0],8))

# def is_palindrome(str):
#     res=''
#     for i in str:
#         res=i+res
#     return str==res
# print(is_palindrome('madam'))

# def count_vowel(text):
#     c=0
#     for j in text:
#         i=j.lower()
#         if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
#             c+=1
#     return c
# print(count_vowel('santoshkumar'))

# def remove_duplicates(nums):
#     r=[]
#     for i in nums:
#         if i not in r:
#             r.append(i)
#     return r
# print(remove_duplicates([1,2,3,2,4,2,3]))

# def most_frequent(nums):
#     d={}
#     for i in nums:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     return max(d,key=d.get)
# print(most_frequent([1,2,3,2,1,2,1,2]))

# def palindrome(s):
#     n=s.lower().replace(" ","")
#     res=''
#     for i in n:
#         res=i+res
#     return n==res
# print(palindrome('A man a plan a canal Panama'))

# def largest(n):
#     h=n[0]
#     for i in n:
#         if i>h:
#             h=i
#     return h
# print(largest([-1,-2,-3,-7,-9,-10]))

# def count_vowels(n):
#     c=0
#     for i in n.lower():
#         if

# def count_vowel(n):
#     m='aeiou'
#     c=0
#     for i in n.lower():
#         if i in m:
#             c+=1
#     return c

def fizz_buzz(m):
    n=[]
    for i in range(1,m+1):
        if i%3==0 and i%5==0:
            n.append('fizzbuzz') 
        elif i%5==0:
            n.append('buzz')
        elif i%3==0:
            n.append('fizz')
        else:
            n.append(i)
    return n
print(fizz_buzz(15))