"""
	account.py
	@author madison flaherty
	@author [YOUR_NAME_HERE]
	Simple bank account model
"""

import generic_testing as t

class Account:
	"""
	Simple account structure
	"""
	name= ""
	kind = "checking"
	
	balance = 0				# intial balance is always 0
	transactions = []		# initially there are no transactions
	
	"""
	NOTE: the "__init__" function is automatically called when you try and initialize
	an instance of your class. It is used to initialize or verify values in that
	particular instance. For now understand that the "self" parameter is
	a reference to your newly made object reference and when manually accessing these methods
	you don't need to supply it ( ie: my_account_obj.get_balance() ). 

	For those particularly interested, you can check out this explanation:
		http://metapython.blogspot.com/2010/11/python-instance-methods-how-are-they.html
	TLDR: instance methods prepend "self" automatically for you so that you don't have
		to do "Account.get_balance(my_account_obj)" every time! 
	"""
	def __init__(self, name, kind, starting_balance):
		""" 
		Initialize the account with a name, kind, and starting balance
		string -> string -> num -> Account
		"""
		self.name = name
		self.kind = kind
		self.balance = starting_balance

	def get_balance(self):
		return self.balance
	
	def get_full_name(self):
		return self.name + " " + self.kind + " Account"

	def get_transactions(self):
		return self.transactions

	
	def add_single_transaction(self, transaction_obj):
		""" Add a single transaction and update the balance accordingly """
		""" STUBBED """
		pass
	
	def add_transactions(self, transactions):
		""" Add multiple transactions """
		""" STUBBED """
		pass
	

"""
TESTING STRUCTURES
"""
"""
NOTE: I would recommend that you always make tests for programs (especially at first) in order
	to make sure that your programs are always providing expected behavior. Making a testing
	structure like this makes your life MUCH easier in the long run and doesn't take long
	once you start figuring it out.
"""
def account_tests():
	""" Tests the account structure """
	test_account = Account('Ally', 'Checking', 0)

	print( t.tester(test_account.get_balance, 0) )
	print( t.tester(test_account.get_full_name, "Ally Checking Account") )
	print( t.tester(test_account.get_transactions, []) )

	print( t.tester(test_account.add_single_transaction, None, [None]) )
	print( t.tester(test_account.add_transactions, None, [[None]]) )

"""
NOTE: the following structure is very common in typical python programs.
	Simple idea here is that only if you run "python3 [this_file_name].py" 
	in the terminal (or wherever) will the "__name__" attribute of this file
	be equal to "__main__". (Essentially only one file can every be "__main__"
	so in the case where there is another file calling on this file, "account_tests"
	will not be run.
	
"""
if __name__ == "__main__":
    account_tests()

