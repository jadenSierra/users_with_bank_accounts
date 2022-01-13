class BankAccount:

    def __init__(self,int_rate=0.02,balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
        elif self.balance < amount:
            print( "Insufficient funds: Charging a $5 fee")
            self.balance -= (amount + 5)
        return self
    def display_account_info(self):
        print(f"Balance:${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.int_rate
        return self

class User:

    def __init__(self, name):
        self.name = name
        self.account = BankAccount()

    def make_deposit(self,amount):
        self.account.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account.balance -= amount
        return self

    def display_user_balance(self):
        print((f"User:{self.name}, Balance: ${self.account.balance}"))
        return self

    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        return self

Rick = User("Rick")
Morty = User("Morty")

Rick.account.display_account_info()
Rick.account.deposit(500).display_account_info()
Rick.account.withdraw(100).display_account_info()
Morty.display_user_balance()