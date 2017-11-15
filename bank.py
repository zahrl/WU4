class BankAccount:
	current_number_of_bank_accounts = 1

	def __init__(self):
		self.account_number = BankAccount.current_number_of_bank_accounts
		BankAccount.current_number_of_bank_accounts += 1;
		self.balance = 0
		print(self.return_account_number() + "New account opened!" + self.return_balance())

	def withdraw(self, amount):
		self.balance -= amount
		print(self.return_account_number() + str(amount) + " withdrawn!" + self.return_balance())
		return self.balance

	def deposit(self, amount):
		self.balance += amount
		print(self.return_account_number() + str(amount) + " deposited!" + self.return_balance())
		return self.balance

	def return_account_number(self):
		return str("Acc.no. " + str(self.account_number) + ": ")

	def return_balance(self):
		return str(" Balance: " + str(self.balance))

a = BankAccount()
b = BankAccount()
a.deposit(100000)
b.deposit(250000)
a.withdraw(1000)
b.withdraw(2000)
