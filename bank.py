class BankAccount:
	current_number_of_bank_accounts = 1

	def __init__(self):
		self.account_number = BankAccount.current_number_of_bank_accounts
		BankAccount.current_number_of_bank_accounts += 1;
		self.__balance = 0
		self.owner = input("Enter name of account holder: ")
		print(self.__return_account_number_and_owner() + "New account opened! " + self.__return_balance())

	def withdraw(self, amount):
		self.__balance -= amount
		print(self.__return_account_number_and_owner() + str(amount) + " withdrawn! " + self.__return_balance())
		return self.__balance

	def deposit(self, amount):
		self.__balance += amount
		print(self.__return_account_number_and_owner() + str(amount) + " deposited! " + self.__return_balance())
		return self.__balance

	def balance(self):
		print(self.__return_account_number_and_owner() + str(self.__return_balance()))

	def __return_account_number_and_owner(self):
		return str("Acc.no. " + str(self.account_number) + " (Acc.holder: " + self.owner + "): ")

	def __return_balance(self):
		return str("Balance: " + str(self.__balance))

a = BankAccount()
b = BankAccount()
a.deposit(100000)
b.deposit(250000)
a.withdraw(1000)
b.withdraw(2000)
a.balance()
b.balance()