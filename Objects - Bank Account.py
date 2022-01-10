class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance



a = BankAccount()
b = BankAccount()

a.deposit(100)
b.deposit(50)
b.withdraw(10)
a.withdraw(10)

print (a.balance)
print (b.balance)

class MinimumBalanceAccount (BankAccount):
    def __init__(self, minimumBalance):
        BankAccount.__init__(self)
        self.minimumBalance = minimumBalance

    def withdraw(self, amount):
        if self.balance - amount < self.minimumBalance: 
            print ('Sorry, below your balance')
        else: 
           BankAccount.withdraw (self, amount)

c = MinimumBalanceAccount (50)
c.deposit (100)
print (c.balance)
c.withdraw(40)
print (c.balance)
c.withdraw (30)


