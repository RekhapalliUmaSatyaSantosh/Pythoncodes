##a=input()
##if len(a)>=8:
##    if any(b.isdigit() for b in a):
##        if any(b.isupper() for b in a):
##            if any(not b.isalnum() for b in a):
##                print('The password is valid')
##            else:
##                print('The password should contain atleast one special character')
##        else:
##            print('The password should contain atleast one capital letter')
##    else:
##        print('The password should contain atleast one number')
##else:
##    print('The password length should contain more than 8')

##a=int(input())
##if a>0:
##    if a%2==0:
##        print('Even number')
##    else:
##        print('Odd number')
##else:
##    print('Not a positive number')

##us=input('Enter username=')
##ps=input('Enter password=')
##if len(us)>=5:
##    if us.isalnum():
##        if not us[0].isdigit():
##            print('Valid Username')
##        else:
##            print('The Username should not start with number')
##    else:
##        print('The Username should not contain any special characters')
##else:
##    print('The length Username should be greater than 5 characters')
##if len(ps)>=8:
##    if any(b.isdigit() for b in ps):
##        if any(b.isupper() for b in ps):
##            if any(not b.isalnum() for b in ps):
##                print('The password is valid')
##            else:
##                print('The password should contain atleast one special character')
##        else:
##            print('The password should contain atleast one capital letter')
##    else:
##        print('The password should contain atleast one number')
##else:
##    print('The password length should contain more than 8')

        
##a,b,c=map(int,input().split())
##if a>b:
##    if a>c:
##        print('Greatest number=',a)
##    else:
##        print('Greatest number=',c)
##else:
##    if b>c:
##        print('Greatest number=',b)
##    else:
##        print('Greatest number=',c)        

##age=int(input('Enter your age='))
##cibilscore=int(input('Enter your cibil score='))
##income=int(input('Enter your monthly income='))
##if 60>age>25:
##    if cibilscore>750:
##        if income>20000:
##            print('Loan Approved')
##        else:
##            print('Not sufficient monthly income')
##    else:
##        print('Not a Good CibilScore')
##else:
##    print('Age is not sufficient')

##n=int(input())
##if n%4==0:
##    if n%100==0:
##        if n%400==0:
##            print('year is divisible by 4, 100, 400')
##        else:
##            print('year is not divisible by 400')
##    else:
##            print('year is not divisible by 100')
##else:
##            print('year is not divisible by 4')
            
##a,b,c=map(int,input().split())
##if not(a+b<=c or b+c<=a or c+a<=b):
##    if not(a==b and b==c):
##        if not(a==b or b==c or c==a):
##            print('Scalene')
##        else:
##            print('Isosceles')
##    else:
##        print('Equilateral')
##else:
##    print('Not a triangle')
##

##exp=int(input('Enter employee experience='))
##per=int(input('Enter employee performance rating='))
##if exp>=5 and per>=5:
##    print('Eligible for High Bonus')
##else:
##    if exp > 3 and per > 4:
##        print('Eligible for Medium Bonus')
##    else:
##        if exp > 1 and per > 1:
##            print('Eligible for Low Bonus')
##        else:
##            print('Eligible for Medium Bonus')

##marks=int(input('Enter student marks='))
##inc=int(input('Enter family income='))
##if marks>=80 and inc<=90000:
##    print('Eligible for High Scholarship')
##else:
##    if marks >= 65 and  inc <= 200000:
##        print('Eligible for Medium Scholarship')
##    else:
##        if marks >= 35 and inc <= 500000:
##            print('Eligible for Low Scholarship')
##        else:
##            print('Not Eligible')

##a=input()
##if a.isalpha():
##    if a.isupper():
##        print('The character is in upper case')
##    else:
##        if a.islower():
##            print('The character is in lower case')
##else:
##    print('The character is not an alphabet')

##ps='admin@123'
##a=input('Enter password=')
##if a==ps:
##    print('Access Granted')
##else:
##    print('Password incorrect, 2 attempts left')
##    b=input('Enter password=')
##    if b==ps:
##        print('Access Granted')
##    else:
##        print('Password incorrect, 1 attempt left')
##        c=input('Enter password=')
##        if c==ps:
##            print('Access Granted')
##        else:
##            print('Access Denied')

##cartamt=int(input('Enter Cart amount='))
##membership=input('Enter type of Membership=').lower()
##if membership=='regular':
##    if cartamt>=1000:
##        val=cartamt*(0.05)
##        price=cartamt-val
##        print('Discount with 5%=',price)
##    else:
##        print('No Discount')
##else:
##    if membership=='silver':
##        if cartamt>=1000:
##            val=cartamt*(0.15)
##            price=cartamt-val
##            print('Discount with 15%=',price)
##        else:
##            print('No Discount')
##    else:
##        if membership=='gold':
##            if cartamt>=1000:
##                val=cartamt*(0.25)
##                price=cartamt-val
##                print('Discount with 25%=',price)
##            else:
##                print('No Discount')
##        else:
##            if membership=='paltinum':
##                if cartamt>=1000:
##                    val=cartamt*(0.30)
##                    price=cartamt-val
##                    print('Discount with 30%=',price)
##                else:
##                    print('No Discount')

