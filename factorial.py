
num=int(input("Enter a number: "))
fact = 1
if num ==0 or num==1:
    print(num)
else:
    for i in range(2,num+1):
        fact*=i
    print(fact)

# import math
# print(math.factorial(5))