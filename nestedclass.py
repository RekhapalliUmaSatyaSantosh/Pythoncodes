# class university:
#     class department:
#         def __init__(self):
#             print('Cse')
# d=university()
# d.department()
# class outer:
#     def __init__(self):
#         print('Outer class object creation.....')
#     class inner:
#         def __init__(self):
#             print('Inner class object creation....')
#         def m1(self):
#             print('Inner class method...')
# o=outer()
# i=o.inner()
# i.m1()
# i=outer().inner()
# i.m1()
# outer().inner().m1()

# class outer:
#     def __init__(self):
#         print('Outer class object....')
#     class inner:
#         def __init__(self):
#             print('Inner class object....')
#         class innerinner:
#             def __init__(self):
#                 print('Innerinner class object...')
#             @staticmethod
#             def m1():
#                 print('Inner class method')
# i=outer().inner().innerinner().m1()
# i=outer()
# n=i.inner()
# m=n.innerinner()
# m.m1()
# outer().inner().innerinner.m1()

# class human:
#     class body:
#         def talk(self):
#             print('Talking.....')
#         class brain:
#             def think(self):
#                 print('Thinking.....')
# o=human()
# i=o.body()
# i.talk()
# n=i.brain().think()

# class human:
#     def __init__(self,name):
#         self.name=name
#         self.head=self.head()
#     def info(self):
#         print('Hello,My self=',self.name)
#         print('I am Full busy with,')
#         self.head.talk()
#         self.head.brain.think()
#     class head:
#         def __init__(self):
#             print('Head object created....')
#             self.brain=self.brain()
#         def talk(self):
#             print('Talking...')
#         class brain:
#             def __init__(self):
#                 print('Brain object created....')
#             def think(self):
#                 print('Thinking.....')
# h=human('Satya')
# h.info()

class person:
    def __init__(self,name,dd,mm,yyyy):
        print('Peron object created....')
        self.name=name
        self.dob=self.Dob(dd,mm,yyyy)
    def info(self):
        print('Name=',self.name)
        self.dob.display()
    class Dob:
        def __init__(self,dd,mm,yyyy):
            print('DOB objr=ect created....')
            self.dd=dd
            self.mm=mm
            self.yyyy=yyyy
        def display(self):
            print(f'DOB={self.dd}/{self.mm}/{self.yyyy}')
p=person('satya',15,3,2005)
p.info()