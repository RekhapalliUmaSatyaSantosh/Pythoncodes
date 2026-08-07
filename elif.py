##a=int(input())
##if a>0:
##    print('positive')
##elif a<0:
##    print('negative')
##else:
##    print('zero')

##a,b,c=map(int,input().split())
##if (a+b)>c and (b+c)>c and (a+c)>b:
##    print('perfect triangle')
##else:
##    print('Not a perfect triangle')

##a=int(input())
##if a>0:
##    j=0
##    for i in range(1,a+1):
##        j+=i
##    print(j)
##elif a<0:
##    print('Negative')
##else:
##    print('zero')
    
##a=int(input())
##if a>0:
##    print(a*(a+1)//2)
##elif a<0:
##    print('Negative')
##else:
##    print('zero')

##marks=int(input())
##if marks>=90:
##    print('A Grade')
##elif marks>=75 and marks<90:
##    print('B Grade')
##elif marks>=50 and marks<75:
##    print('C Grade')
##elif marks>=35 and marks<50:
##    print('D Grade')
##else:
##    print('Fail')

##a,b,c=map(int,input().split())
##if a>b and a>c:
##    print('Greatest number=',a)
##elif b>c:
##    print('Greatest number=',b)
##else:
##    print('Greatest number=',c)

##age=int(input('Enter your age='))
##if age<12:
##    print('Child')
##elif age>12 and age<20:
##    print('Teen')
##elif age>19 and age<60:
##    print('Adult')
##else:
##    print('Senior')

##a,b=map(int,input('Enter two daybers=').split())
##sign=input('Enter mathematical symbol=')
##if sign=='+':
##    print('The answer =',a+b)
##elif sign=='-':
##    print('The answer =',a-b)
##elif sign=='*':
##    print('The answer =',a*b)
##elif sign=='/':
##    print('The answer =',a/b)

##day=input('Enter the day=')
##if day=='1':
##    print('Monday')
##elif day=='2':
##    print('Tuesday')
##elif day=='3':
##    print('Wednesday')
##elif day=='4':
##    print('Thursday')
##elif day=='5':
##    print('Friday')
##elif day=='6':
##    print('Saturday')
##elif day=='7':
##    print('Sunday')

##balance=10000
##amount=int(input('Enter amount to withdrawal='))
##if balance>amount:
##    print('Withdrawal successful')
##    print('New balance amount=',(balance-amount))
##elif amount>balance:
##    print('Insufficient funds')
##else:
##    print('Zero balance')

##signal=input('Enter signal-light color=')
##if signal.lower()=='red':
##    print('Stop')
##elif signal.lower()=='yellow':
##    print('Be Ready')
##elif signal.lower()=='green':
##    print('Go')

##bmi = float(input())
##if bmi < 18.5:
##    print('Underweight')
##elif 18.5 <= bmi <= 24.9:
##    print('Healthy Weight')
##elif 25.0 <= bmi <= 29.9:
##    print('Overweight')
##elif 30.0 <= bmi <= 34.9:
##    print('Obese Class I')
##elif 35.0 <= bmi <= 39.9:
##    print('Obese Class II')
##else:
##    print('Obese Class III')

##unit=int(input('Enter how many units='))
##if 0<unit<=100:
##    print('Amount=',unit*2)
##elif 101<unit<=300:
##    print('Amount=',unit*4)
##else:
##    print('Amount=',unit*8)

##a,b,c=map(int,input().split())
##if (a>=c and a<=b) or (a<=c and a>=b):
##    print('Second largest number=',a)
##elif (b>=c and b<=a) or (b<=c and b>=a):
##    print('Second largest number=',b)
##else:
##    print('Second largest number=',c)

##ticket=int(input('Enter your count of tickets='))
##price=300
##age=int(input('Enter your age='))
##day=input('Enter day=')
##if day in ['saturday','sunday']:
##    print('The ticket price with tax=',(price*ticket)+200)
##elif age>60:
##    print('The ticket with discount=',(price*ticket)-150)
##else:
##    print('The ticket price=',(price*ticket))

##a,b,c=map(int,input().split())
##d=b*b-4*a*c
##if d>0:
##    r1=(-b + d**0.5)/(2*a)
##    r2=(-b - d**0.5)/(2*a)
##    print('Two distinct real roots=',r1,r2)
##elif d==0:
##    r=-b/(2*a)
##    print('The root=',r)
##elif d<0:
##    rl=-b/(2*a)
##    ip=(abs(d)**0.5)/(2*a)
##    print('Two complex roots:')
##    print(rl,'+',ip,'i')
##    print(rl,'-',ip,'i')

##temp=int(input())
##if temp<4:
##    print('Freezing')
##elif 4<temp<15:
##    print('Cold')
##elif 15<temp<27:
##    print('Warm')
##elif 27<temp<40:
##    print('Hot')
##elif temp>40:
##    print('Extreme hot')



