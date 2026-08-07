# class Animal:
#     def eat(self):
#         print("Animal is eating")

# class Bird:
#     def fly(self):
#         print("Bird is flying")

# class Sparrow(Animal, Bird):
#     def chirp(self):
#         print("Sparrow is chirping")

# # Example usage
# s = Sparrow()

# s.eat()
# s.fly()
# s.chirp()

# class rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def rect(self):
#         print(f"Length : {self.length}, and Width: {self.width} ")
# class square:
#     def __init__(self,side):
#         self.side=side
#     def sqr(self):
#         print(f"Side : {self.side}")
# class circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def cir(self):
#         print(f"Radius : {self.radius}")
# class area(rectangle,square,circle):
#     def __init__(self,length,width,side,radius):
#         rectangle.__init__(self, length, width)
#         square.__init__(self, side)
#         circle.__init__(self, radius)
#     def display(self):
#         print("The Area of rectangle is:",self.length*self.width)
#         print("The Area of square is:",self.side*self.side)
#         print("The Area of circle is:",3.14*self.radius*self.radius)
# obj=area(10,11,12,13)
# obj.rect()
# obj.sqr()
# obj.cir()
# obj.display()


# class rectangle:
#     def rect(self):
#         self.length=int(input("Enter lenght:"))
#         self.width=int(input("Enter width:"))
# class square:
#     def sqr(self):
#         self.side=int(input("Enter side:"))
# class circle:
#     def cir(self):
#         self.radius=int(input("Enter radius:"))
# class area(rectangle,square,circle):
#     def display(self):
#         print("The Area of rectangle is:",self.length*self.width)
#         print("The Area of square is:",self.side*self.side)
#         print("The Area of circle is:",3.14*self.radius*self.radius)
# obj=area()
# obj.rect()
# obj.sqr()
# obj.cir()
# obj.display()

# class stuname:
#     def sname(self):
#         self.name=str(input(""))
# class sturollno:
#     def srollno(self):
#         self.rollno=int(input(""))
# class marks:
#     def smarks(self):
#         self.marks1=int(input(""))
#         self.marks2=int(input(""))
#         self.marks3=int(input(""))
#         self.marks4=int(input(""))
#         self.marks5=int(input(""))
# class student(stuname,sturollno,marks):
#     def display(self):
#         print("The name of student is:",self.name)
#         print("The rollnum is:",self.rollno)
#         print("The marks in subject1:",self.marks1)
#         print("The marks in subject2:",self.marks2)        
#         print("The marks in subject3:",self.marks3)
#         print("The marks in subject4:",self.marks4)        
#         print("The marks in subject5:",self.marks5)
# obj=student()
# obj.sname()
# obj.srollno()
# obj.smarks()
# obj.display()

# class a:
#     def __init__(self):
#         print("This is class A")
# class b:
#     def __init__(self):
#         print("This is class B")
# class c(b,a):
#     def display(self):
#         print("This is class C")
# obj=c()
# obj.display()

class Solution:
    def checkStatus(self, a, b, flag):
        # code 
        if a>0 and b<0 and not flag:
            print(True)
        else:
            print(False)
output=Solution()
output.checkStatus(1,-2,False)