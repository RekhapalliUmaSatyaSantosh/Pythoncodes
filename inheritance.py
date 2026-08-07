# '''multilevel inherintnace'''
# class BankAccount:
#     def __init__(self, acc, bal, pin):
#         self.acc=acc
#         self.bal=bal
#         self.pin=pin
# class Savings(BankAccount):
#     def __init__(self, acc, bal, pin):
#         if bal>=1000:
#             super().__init__(acc, bal, pin)
#         else:
#             print('Insufficient funds ')
# class Childsavings(Savings):
#     def __init__(self, acc, bal, pin, age):
#         if age>11 and age<18:
#             super().__init__(acc, bal, pin)
#             self.age=age
#         else:
#             print('Not sufficient age')
# user1=Childsavings(1233,1400,1243,13)

# '''multiple inheritance'''
class BankAccount:
    def __int__(self,acc,bal):
        self.acc=acc
        self.bal=bal
    def deposit(self,amount):
        self.bal+=amount
class Loan:
    def __init__(self,p,t,r):
        self.pcpa=p
        self.time=t
        self.roi=r
    def interest(self):
        return (self.pcpa*self.time*self.roi/100)
class Loanacc(Loan,BankAccount):
    def __int__(self, acc, bal):
        super().__int__(acc, bal)
        BankAccount.__init__(self,acc,bal)
    def deposit(self, amount):
        if amount<=self.pcpa:
            return super().deposit(amount)
        else:
            print('Cannot deposite more than pcpa')
la1=Loanacc(100000,4,15,13579,2000)
la1.deposit(10000)