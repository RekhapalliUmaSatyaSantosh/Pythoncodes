# # class A:
# #     def disply(self):
# #         print("Thuis is class A")

# # obj=A()
# # A.disply(obj)

# class dog:
#     def details(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("Dog name is:",self.name)
#         print("Dog age is:",self.age)
# dog1=dog()
# dog1.details("Tommy",5)
# dog1.display()

# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def displdisplayay(self):
#         print(f"Dog name is: {self.name} and age is: {self.age}")
# obj=Dog("Tommy",5)
# obj2=Dog("Max",3)
# obj3=Dog("Buddy",4)
# print(obj.display(),obj2.(),obj3.display())

# class test:
#     def __init__(self):
#         print("Object of self:",id(self))
# t=test()
# print("Object of test:",id(t))

# class test:
#     def __init__(self):
#         print('Constructor')
# t=test()
# t.__init__()

# class test:
#     def __init__(self):
#         print('no-arg construvtor')
#     def __init__(sekf,x):
#         print('One-arg constructor')
# # t=test()
# t=test(10)

# class movie:
#     def __init__(self,title,hero,herione):
#         self.title=title
#         self.hero=hero
#         self.herione=herione
#     def info(self):
#         print('Movie name=',self.title)
#         print('Hero name=',self.hero)
#         print('Herione name=',self.herione)
# list_of_movies=[]
# while True:
#     title=input('Movie name=')
#     hero=input('Hero name=')
#     herione=input('Herione name=')
#     m=movie(title,hero,herione)
#     list_of_movies.append(m)
#     print('Movies added to list successfully....')
#     option=input('do you want to add one more movie [yes] [no]:')
#     if option.lower() == 'no':
#         break
# print('All movies information...')
# for movie in list_of_movies:
#     movie.info()
#     print()

# class test:
#     def test(self):
#         print('constructor')
# t=test()
# t.test()

# class student:
#     @classmethod
#     def m1(cls):
#         print(id(cls))
# test=student()
# print(id(test))
# test.m1()

# class student:
#     schoolname='Aditya'
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#     def getinfo(self):
#         print('Student name:',self.name)#it is instance method becoz we have used the instance varibale i.e; self.name
#         print('Student rollno:',self.rollno)
#     @classmethod
#     def getname(cls):
#         print('School name:',cls.schoolname)#it is class method becoz we have used the static variable and first variable is cls
#     @staticmethod 
#     def getsum(a=10,b=20):
#         sum=a+b
#         return sum
# test=student('suresh',90)
# test.getinfo()
# test.getname()
# print(test.getsum())

# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#     def m1(self):
#         self.c=30
# t=test()
# t.m1()
# t.d=40
# t1=test()
# print(t.__dict__)
# print(t1.__dict__)

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display(self):
#         print('Hello',self.name)
#         print('Your Marks are:',self.marks)
#     def grade(self):
#         if self.marks>=60:
#             print('You got First Grade')
#         elif self.marks>=50:
#             print('You got Second Grade')
#         elif self.marks>=35:
#             print('You got Third Grade')
#         else:
#             print('You are Failed')
# n=int(input('Enter no.of students='))
# for i in range(n):
#     name=input('Enter student name=')
#     marks=int(input('Enter your marks='))
#     s=student(name,marks)
#     s.display()
#     s.grade()
#     print()

# class student:
#     def setname(self,name):
#         self.name=name
#     def getname(self):
#         return  self.name
#     def setmarks(self,marks):
#         self.marks=marks
#     def getmarks(self):
#         return self.marks
# n=int(input('Enter no.of students='))
# students=[]
# for i in range(n):
#     s=student()
#     name=input('Enter student name=')
#     marks=int(input('Enter marks='))
#     s.setname(name)
#     s.setmarks(marks)
#     students.append(s)
# for s in students:
#     print('Hello',s.getname())
#     print('Your marks=',s.getmarks())
#     print()

# class test:
#     count=0
#     def __init__(self):
#         test.count=test.count+1
#     @classmethod
#     def getnoofobj(cls):
#         print("The no.of objs=",cls.count)
# test.getnoofobj()
# t1=test()
# t2=test()
# t3=test()
# test.getnoofobj()


# class math:
#     @staticmethod
#     def add(a,b):
#         print(f'The sum of {a} and {b}={a+b}')
#     @staticmethod
#     def product(a,b):
#         print(f'The product of {a} and {b}={a*b}')
#     @staticmethod
#     def avg(a,b):
#         print(f'The avg of {a} and {b}={(a+b)/2}')
# math.add(10,20)
# math.product(10,20)
# math.avg(10,20)

