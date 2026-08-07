class a:
    pass
class b:
    pass
class c:
    pass
class d(a,b):
    pass
class e(b,c):
    pass
class f(d,e):
    pass
print(f.__mro__)
# class mammals:
#     def info(self):
#         print("Mammals can birth to babies")
# class winged:
#     def info(self):
#         print("winged animals can fly")
# class bat(mammals,winged):
#     pass
# obj=bat()
# obj.info()

# class mammals:
#     def info(self):
#         print("Give birth to babies")
# class fishes:
#     def info(self):
#         print("These live in water")
# class reptiles:
#     def info(self):
#         print("cool blooded animals and lay eggs")
# class amphibians:
#     def info(self):
#         print("Animals that live in both water and land")
# class birds:
#     def info(self):
#         print("These can fly and lay eggs")
# class whales(mammals,fishes):
#     pass
# class frog(reptiles,amphibians):
#     pass
# class hen(birds,reptiles,amphibians):
#     pass
# obj=hen()
# obj.info()

# class a:
#     def info(self):
#         self.firstname=str(input("enter names"))
# class b:
#     def info(self):
#         self.surname=str(input("enter your surname"))
# class c:
#     def info(self):
#         self.lastname=str(input("enter your last name"))
# class d(a,b):
#     def values(self):
#         print(self.firstname)
#         print(self.surname)
# class e(b,c):
#     def values(self):
#         print(self.surname)
#         print(self.lastname)
# class f(d,e,c):
#     pass
# obj=f()
# obj.values()