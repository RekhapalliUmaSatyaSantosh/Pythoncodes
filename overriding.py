# class test:
#     def property(self):
#         print('land + gold + cash + power')
#     def marry(self):
#         print('keerthy suresh')
# class test1(test):
#     def marry(self):
#         super().marry()
#         print('priyanka mohan')
# c=test1()
# c.property()
# c.marry()

# class P:
#     def __init__(self):
#         print('Parent constructor')
# class C(P):
#     def __init__(self):
#         super().__init__()
#         print('Child constructor')
# c=C()

# class person:
#     def __init__(self,name,age,height,weight):
#         self.name=name
#         self.age=age
#         self.height=height
#         self.weight=weight
#     def display(self):
#         print('Name=',self.name)
#         print('Age=',self.age)
#         print('Height=',self.height)
#         print('Weight=',self.weight)
# class employee(person):
#     def __init__(self,name,age,height,weight,eno,esal):
#         super().__init__(name,age,height,weight)
#         self.eno=eno
#         self.esal=esal
#     def display(self):
#         super().display()
#         print('Employee no=',self.eno)
#         print('Employee sal=',self.esal)
# e=employee('Satya',23,'68kgs',5.10,1232134,10000)
# e.display()

class vehicle:
    def typeofvehicle(self):
        self.type = int(input('Enter Number of wheels='))

    def wheelsofvehicle(self):
        if self.type == 2:
            print('Motor Bike')
        elif self.type == 3:
            print('Auto')
        elif self.type == 4:
            print('Car')
        elif self.type>4:
            print('Bus or Lorry')

v = vehicle()
v.typeofvehicle()
v.wheelsofvehicle()