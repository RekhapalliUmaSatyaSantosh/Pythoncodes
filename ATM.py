class atm:
    def __init__(self,initial_balance=1000,pin='1234'):
        self.balance=initial_balance
        self.pin=pin
        self.is_authenticated=False

    def authenticate(self,enterpin):
        if enterpin==self.pin:
            self.is_authenticated=True
            print("Authentication successful!")
        else:
            print('Authentication failed. Please try again.')

    def check_balance(self):
        if self.is_authenticated:
            print(f'Your current balance=${self.balance:.2f}')
        else:
            print('Authenticate first')

    def withdraw(self,amount):
        if not self.is_authenticated:
            print('Authenticate first')
            return
        if amount > self.balance:
            print('Insufficient funds')
        elif amount <= 0:
            print('Withdrawal amount must be positive')
        else:
            self.balance -= amount
            print(f'Successfully withdrew: {amount:.2f}')
            print(f'Your new balance is: {self.balance:.2f}')

    def deposite(self,amount):
        if not self.is_authenticated:
            print('Authenticate first')
            return
        if amount<=0:
            print('Deposit amount must be positive')
        else:
            self.balance += amount
            print(f'Successfully deposited: {amount:.2f}')
            print(f'Your new balance is: {self.balance:.2f}')
a=atm()
authenticated = False
while not authenticated:
    print("\nPlease authenticate to proceed.")
    pin_input = input("Enter your PIN: ")
    a.authenticate(pin_input)
    authenticated = a.is_authenticated 

while True:
    print("\n--- Menu ---")
    print("c - Check Balance")
    print("d - Deposit")
    print("w - Withdraw")
    print("e - Exit")
    choice=input("Enter your Choice: ")

    if choice.lower()=='c':
        a.check_balance()
    elif choice.lower()=='d':
        try:
            amount=float(input('Enter amount to deposit: '))
            a.deposite(amount)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice.lower()=='w':
        try:
            amount=float(input('Enter amount to withdraw: '))
            a.withdraw(amount)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice.lower()=='e':
        print('Thanks for using ATM! Visit Again......')
        break
    else:
        print('Please choose a valid option.')
