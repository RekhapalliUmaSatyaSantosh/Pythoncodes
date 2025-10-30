# class rectangle:
#     def __init__(self,height,width):
#         self.height=height
#         self.width=width
#     def display(self):
#         print(f"Height: {self.height}, and Width: {self.width}")
# class area(rectangle):
#     def __init__(self,height,width):
#         super().__init__(height,width)
#     def display(self):
#         super().display()
#         print("Area is: ",self.height*self.width)
# class perimeter(area):
#     def __init__(self,height,width):
#         super().__init__(height,width)
#     def display(self):
#         super().display()
#         print("Perimeter is:",(self.height+self.width)*2)
# # obj=area(10,11)
# obj2=perimeter(10,11)
# obj2.display()

# class circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def display(self):
#         print("Radius is:",self.radius)
# class area(circle):
#     def __init__(self,radius):
#         super().__init__(radius)
#     def display(self):
#         super().display()
#         print("Area is:", 3.14*self.radius*self.radius)
# class perimeter(area):
#     def __init__(self,radius):
#         super().__init__(radius)
#     def display(self):
#         super().display()
#         print("Perimeter is:",2*self.radius*3.14)
# obj=perimeter(5)
# obj.display()

class a:
    def __init__(self):
        print("This is class A")
class b(a):
    def __init__(self):
        super().__init__()
        print("This is class B")
class c(b):
    def __init__(self):
        super().__init__()
        print("This is class C")
obj=c()