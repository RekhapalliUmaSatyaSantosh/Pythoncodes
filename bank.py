class customer:
    """                   This class developed by Santosh and describes bank applications"""
    bankname="SatyaSantosh BANK"
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposite(self,amount):
        self.balance=self.balance+amount
        print("After Deposite the balance=",self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient Funds")
        else:
            self.balance=self.balance-amount
            print("The balance=",self.balance)
print('='*100)
print(customer.__doc__)
print('='*100)
print("welcome to",customer.bankname)
name=input("Enter your Name=")
c=customer(name)
while True:
    print("d-Desposite \nw-Withdrawl \ne-Exit")
    choice=input("Enter you Choice=")
    if choice.lower()=='d':
        amount=float(input('Enter amount to deposite='))
        c.deposite(amount)
    elif choice.lower()=='w':
        amount=float(input('Enter amount to withdraw='))
        c.withdraw(amount)
    elif choice.lower()=='e':
        print('Thanks for Banking......')
        break
    else:
        print('Please choose valid option=')