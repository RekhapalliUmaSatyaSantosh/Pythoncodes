# class school:
#     schoolname='Aditya school'
#     add='Palakollu'
    

# class BankAccount:
#     def __init__(self, acc, bal, pin, age):
#         self.acc=acc
#         self.bal=bal
#         self.pin=pin
#         self.age=age
#     def deposite(self,amount):
#         self.amount=amount
# class Savings(BankAccount):
#     def __init__(self, acc, bal, pin, age):
#         if age>=20:
#             super().__init__(acc,bal,pin,age)
#         else:
#             return 'Age is not sufficient'
#     def deposite(self, amount):
#         super().deposite(amount)
#         if amount>500:
#             self.bal+=amount
#             print(f'new balance={self.bal}')
    # @staticmethod
    # def valid(n):
    #     if isinstance(n,(int, float)):
    #         if n>0:
    #             return True
    #     return False
# user1=Savings(12416654,1100,1356,21)
# user1.deposite(1000)