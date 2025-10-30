# class a:
#     def __init__(self):
#         print("This is class a")
# class b(a):
#     def display(self):
#         print("This is class b")
# obj = b()
# obj.display()

# class animal:
#     def __init__(self, name,sound):
#         self.name = name
#         self.sound = sound
#     def display(self):
#         print(f"Dog Name: {self.name}, Sounds like: {self.sound}")
# class dog(animal):
#     def __init__(self,name,sound, age):
#         # self.model=model
#         # self.year=year
#         super().__init__(name,sound)
#         self.age = age

#     def display(self):
#         super().display()
#         print(f"Age is: {self.age} years old")
# obj = dog("Tommy", "bow", 10)
# obj.display()
class a:
    def __init__(self):
        print("This is class A")
class b(a):
    def display(self):
        print("This is class B")
obj = b()
obj.display()