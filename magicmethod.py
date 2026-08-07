# class p:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def __gt__(self,other):
#         return self.marks>other.marks
#     def __le__(self,other):
#         return self.marks<=other.marks
# c1=p('satya',55)
# c2=p('santosh',40)
# print(c1>c2)
# print(c2<=c1)

# class book:
#     def __init__(self,pages):
#         self.pages=pages
#     def __add__(self,other):
#         return book(self.pages+other.pages)
#     def __mul__(self,other):
#         return book(self.pages*other.pages)
#     def __str__(self):
#         return f'The total no.of pages={self.pages}'
# b1=book(564)
# b2=book(789)
# b3=book(778)
# print(b1+b2)
# print(b1*b2+b3)

# class employee:
#     def __init__(self,name,salaryperday):
#         self.name=name
#         self.salaryperday=salaryperday
#     def __mul__(self,other):
#         return self.salaryperday*other.workingdays
# class timesheet:
#     def __init__(self,name,workingdays):
#         self.name=name
#         self.workingdays=workingdays
#     def __mul__(self,other):
#         return self.workingdays*other.salaryperday
        
# e=employee('Satya',5000)
# t=timesheet('Satya',30)
# print('This month salary=',e*t)
# print(t*e)

# class student:
#     def __init__(self,name,rollno,marks):
#         self.name=name
#         self.rollno=rollno
#         self.marks=marks
#     def __str__(self):
#         # return self.name
#         return f'name={self.name},rollno={self.rollno},marks={self.marks}'
# s1=student('satya',100,98)
# s2=student('Santosh',101,99)
# print(s1)
# print(s2)

# class test:
#     def m1(self):
#         print('No args')
#     def m1(self,a):
#         print('One arg')
#     def m1(self,a,b):
#         print('Two args')
# t=test()
# t.m1(1,2)

# class test:
#     def m1(self,x=None,y=None,z=None):
#         if x is not None and y is not None and z is not None:
#             print('Three arg enthod')
#         elif x is not None and y is not None:
#             print('Two args method')
#         elif x is not None:
#             print('One arg method')
#         else:
#             print('No arg method')
            
# t=test()
# t.m1(10,20,30)

# class test:
#     def m1(self,*args):
#         print('Args method')
# t=test()
# t.m1(10)
# t.m1(1.0,2.0)
# t.m1(10,20,30)
# t.m1(10,20,30,40)
# t.m1(10,20)
# t.m1(10,20)
# t.m1(10,20)

# class test:
#     def m1(self,x):
#         print(f'Args method={x.__class__.__name__}')
# t=test()
# t.m1(10)
# t.m1(1.0)
# t.m1('s')
# t.m1([10])
# t.m1((10))
# t.m1({10})
# t.m1({10:2})

# class test:
#     # def sum(self,*args):
#     #     tot=0
#     #     for x in args:
#     #         tot=tot+x
#     #     print('The total=',tot)
#     # def min(self,*args):
#     #     tot=0
#     #     for x in args:
#     #        tot=tot-x
#     #     print('The total=',tot)
#     def mul(self,*args):
#         tot=0
#         for x in args:
#            tot=tot*x
#         print('The total=',tot)
#     def div(self,*args):
#         tot=0
#         for x in args:
#            tot=tot/x
#         print('The total=',tot)
#     def mod(self,*args):
#         tot=0
#         for x in args:
#            tot=tot//x
#         print('The total=',tot)
#     def pow(self,*args):
#         tot=0
#         for x in args:
#            tot=tot**x
#         print('The total=',tot)
    

# t=test()
# # t.sum(10,20,30)
# # t.min(10,5)
# t.mul(10,20)
# t.div(20,10)
# t.mod(20,10)
# t.pow(10,2)

class test:
    def __init__(self,a=None,b=None,c=None):
        print('Consturctor with 0/1/2/3 arguments')
    def __init__(self,*args):
        print('hello')
t=test()
t=test(10)
t=test(10,20)
t=test(10,20,30,40)
