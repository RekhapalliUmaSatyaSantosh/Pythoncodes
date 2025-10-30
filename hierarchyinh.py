# class square:
#     def __init__(self,side):
#         self.side=side
#     def display(self):
#         print(f"Enter side value: {self.side}")
# class area(square):
#     def __init__(self,side):
#         super().__init__(side)
#     def display(self):
#         super().display()
#         print("Area of square is:",self.side*self.side)
# class perimeter(square):
#     def __init__(self,side):
#         super().__init__(side)
#     def display(self):
#         super().display()
#         print("Perimeter of square is:",self.side*4)
# obj=area(4)
# obj.display()
# obj2=perimeter(5)
# obj2.display()

# class atm:
#     def __init__(self):
#         self.balance=0
#         print("Account is created")
#     def deposite(self):
#         amount=int(input("Enter amount to deposite:"))
#         self.balance=self.balance+amount
#         print("Balance is:",self.balance)
#     def withdrawl(self):
#         amount=int(input("Enter amount to withdraw:"))
#         if amount>self.balance:
#             print("Insuuficient Funds")
#         else:
#             self.balance=self.balance-amount
#             print("New Balance is:",self.balance)
#     def enqury(self):
#         num=input("Do you want check your balance:(yes/No)")
#         if num=='yes' or num=='y':
#             print("Balance is:",self.balance)
#         else:
#             print("Thank you")
# obj=atm()
# obj.deposite()
# obj.withdrawl()
# obj.enqury()

class a:
    def __init__(self):
        print("This is class A")
class b(a):
    def display(self):
        # super().__init__()
        print("This is class B")
class c(a):
    def __init__(self):
        print("This is class C")
obj=b()
obj.display()
obj1=c()
