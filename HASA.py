# class Engine:
#     def m1(self):
#         print('Specific engine')
# class Car:
#     def __init__(self):
#         print('This is Car')
#         self.engine=Engine()
#     def m2(self):
#         self.engine.m1()
# c=Car()
# c.m2()

# class Car:
#     def __init__(self,name,model,color):
#         self.name=name
#         self.model=model
#         self.color=color
#     def carinfo(self):
#         print(f'Car Name={self.name}, Car model={self.model}, Car color={self.color}')
# class Employee:
#     def __init__(self,ename,eno,car):
#         self.ename=ename
#         self.eno=eno
#         self.car=car
#     def empinfo(self):
#         print(f'Employee Name={self.ename}, Employee Number={self.eno}')
#         print('Employee Car info=')
#         self.car.carinfo()
# c=Car('Mahindra','XUV700','Black')
# e=Employee('Suresh',872992,c)
# e.empinfo()

# class Sportsnews:
#     def sportsinfo(self):
#         print('Sports INformation-1')
#         print('Sports INformation-2')
#         print('Sports INformation-3')
#         print('Sports INformation-4')
# class Politicnews:
#     def politicinfo(self):
#         print('='*100)
#         print('Political INformation-1')
#         print('Political INformation-2')
#         print('Political INformation-3')
#         print('Political INformation-4')
# class Movienews:
#     def moviesinfo(self):
#         print('='*100)
#         print('Movies INformation-1')
#         print('Movies INformation-2')
#         print('Movies INformation-3')
#         print('Movies INformation-4')
# class Newschannel:
#     def __init__(self,sports,politics,movies):
#         # self.sports=Sportsnews()
#         # self.politics=Politicnews()
#         # self.movies=Movienews()
#         self.sports=sports
#         self.politics=politics
#         self.movies=movies
#     def getinfo(self):
#         self.sports.sportsinfo()
#         self.politics.politicinfo()
#         self.movies.moviesinfo()
# sn=Sportsnews()
# pn=Politicnews()
# mn=Movienews()
# nc=Newschannel(sn,pn,mn)
# nc.getinfo()

class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def getinfo(self):
        print(f'\tCar Name={self.name}\n \tModel={self.model}\n \tcolor={self.color}')
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eatndrink(self):
        print('Eating Briyani and Drinking Thumsup')
class Employee(Person):
    def __init__(self,name,age,eno,esal,car):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
        self.car=car
    def work(self):
        print('Coding Python Programming')
    def empinfo(self):
        print('Employee Name=',self.name)
        print('Employee Age=',self.age)
        print('Employee Number=',self.eno)
        print('Employee Salary=',self.esal)
        print('Employee Car information')
        self.car.getinfo()
car=Car('Innova','2.5v','Black')
e=Employee('Satya',48,8724332,10000,car)
e.eatndrink()
e.work()
e.empinfo()