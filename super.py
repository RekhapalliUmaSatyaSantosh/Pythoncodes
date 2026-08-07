# class p:
#     a=10
#     def __init__(self):
#         print('Parent class')
#     def m1(self):
#         print('Parent Instance class')
#     @staticmethod
#     def m2():
#         print('Parent static method')
#     @classmethod
#     def m3(cls):
#         print('Parent Class method')
# class c(p):
#     def __init__(self):
#         print('Child class')
#     def method(self):
#         print(self.a)
#         self.m1() or super().m1()
#         self.m2() or super().m2()
#         self.m3() or super().m3()
#         super().__init__()
# cl=c()
# cl.method()

class person:
    def __init__(self,name,age,weight,height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
    def display(self):
        print('Name=',self.name)
        print('Age=',self.age)
        print('Weight=',self.weight)
        print('Height=',self.height)
class student(person):
    def __init__(self,name,age,weight,height,rollno,marks):
        super().__init__(name,age,weight,height)
        self.rollno=rollno
        self.marks=marks
    def display(self):
        super().display()
        print('Rollno=',self.rollno)
        print('marks=',self.marks)
s=student('Satya',21,'68kg','175cm','22JD1A05A0',588)
s.display()        