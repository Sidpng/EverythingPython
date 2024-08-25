class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            return "The balance is insufficient"
        else:
            self.balance = self.balance - amount
            return self.balance

    def check_balance(self):
        return self.balance

ownerName = input("Enter your name as per bank records: ")
balanceAmount =  int(input("Enter the balance of the account: "))
withdrawAmount = int(input("Enter the amount you want to withdraw: "))
depositAmount = int(input("Enter the amount you want to deposit: "))

bankAccount = BankAccount(ownerName, balanceAmount)
print(bankAccount.check_balance())
print(bankAccount.withdraw(withdrawAmount))
print(bankAccount.deposit(depositAmount))
print(bankAccount.check_balance())