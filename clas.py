# class addition:
#     def add(self,a,b):
#         return a + b
# ob = addition()
# print(ob.add(10,5))

# class rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length*self.width
#     def perimeter(self):
#         return (self.length*self.width)//2
    
# ob = rectangle(10,5)
# print(ob.area())
# print(ob.perimeter())

# class student:
#     def __init__(self,name,rollno,courses):
#         self.name=name 
#         self.rollno=rollno
#         self.courses=courses
#     def display(self):
#         print(f"Name: {self.name}, Roll No: {self.rollno}, Courses: {', '.join(self.courses)}")
# ob = student("John Doe", 101, ["Math", "Science", "English"])
# print(ob.display())

# class dog:
#     def __init__(self):
#         print("This is a dog class")
# obj=dog()

# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#         self.c=30
#         self.d=40
    # def display(self):
    #     # print(self.a,self.b,self.c,self.d)
    #     del self.c
# t=test()
# t.a=233
# t.b=333
# print(t.__dict__)
# t1=test()
# print(t1.__dict__)

# class test:
#     a=10
#     def __init__(self):
#         test.b=20
#     def m1(self):
#         test.c=30
#     @classmethod
#     def m2(cls):
#         cls.d=40
#         test.e=50
#     @staticmethod
#     def m3():
#         test.f=60
# t=test()
# t.m1()
# t.m2()
# t.m3()
# test.g=70
# print(test.__dict__)

# class test:
#     a=10
#     def __init__(self):
#         print('By using self variable in a constructor',self.a)
#         print('By using classname in a constructor',test.a)
#     def m1(self):
#         print('By using self in a instance method',self.a)
#         print('By using classname in a instance method',test.a)
#     @classmethod
#     def m2(cls):
#         print('By using cls in a class method',cls.a)
#         print('By using classname in a class method',test.a)
#     @staticmethod
#     def m3():
#         print('By using classname in a static method',test.a)
# t=test()
# t.m1()
# t.m2()
# t.m3()
# print('By using obj refernce outside class',t.a)
# print('By using classname outside class',test.a)

# class test:
#     a=10
#     def __init__(self):
#         test.a=20
#     def m1(self):
#         test.a=30
#     @classmethod
#     def m2(cls):
#         cls.a=40
#         test.a=50
#     @staticmethod
#     def m3():
#         test.a=60
# t=test()
# t.m1()
# t.m2()
# t.m3()
# test.a=70
# print(test.a)

# class test:
#     a=10
#     def __init__(self):
#         self.b=20
#     def m1(self):
#         self.a=888
#         self.b=999
# t1=test()
# t2=test()
# t1.m1()
# t2.m1()
# print(t1.a,t1.b)
# print(t2.a,t2.b)
# test.a=888
# test.b=999
# print(t1.a,t1.b)
# print(t2.a,t2.b)
# print(test.a,test.b)

# class test:
# a=10
#     @classmethod
#     def m1(cls):
#         # del test.a
#         pass
# t=test()
# test.a
# print(test.__dict__)

# class test:
#     @staticmethod
#     def average(list1):
#         res=sum(list1)/len(list1)
#         print("The Sum=",sum(list1))
#         print("The Length=",len(list1))
#         print("The Average=",res)
#     @staticmethod
#     def wish(name):
#         for i in range(10):
#             print("Good Morning",name)
# list1=[10,20,30,40,50]
# test.average(list1)
# test.wish('Durga')

# class employee:
#     def __init__(self,eno,ename,esal):
#         self.eno=eno
#         self.ename=ename
#         self.esal=esal
#     def display(self):
#         print('Employee number =',self.eno)
#         print('Employee name =',self.ename)
#         print('Employee salary =',self.esal)
# class manager:
#     def update(emp):
#         emp.esal=emp.esal+10000
#         emp.display()
# emp=employee(101,'Suresh',12000)
# manager.update(emp)


