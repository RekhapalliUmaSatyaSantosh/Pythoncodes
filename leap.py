# year=int(input())
# if (year%4==0 and year%100!=0)or(year%400==0):
#     print("Leap Year")
# else:
#     print("Not Leap Year")

# def leap():
#     year=int(input())
    # if(year%4==0 and year%100!=0)or(year%400==0):
#         print("Leap year")
#     else:
#         print("Not Leap year")
# leap()

# class leap:
#     def display(self):
#         self.year=int(input())
#         if(self.year%4==0 and self.year%100!=0)or(self.year%400==0):
#             print("Leap Year")
#         else:
#             print("Not Leap Year")
# l=leap()
# l.display()

n=int(input())
if n>0:
    for i in range(1,n+1):
        print(i,end='')
else:
    print("Enter valid integer")