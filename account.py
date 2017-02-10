"""
	account.py
	@author madison flaherty
	Simple bank account model
"""

class Account:
	"""
	Simple account structure
	"""
	name= ""
	kind = "checking"
	
	balance = 0				# intial balance is always 0
	transactions = []		# initially there are no transactions
	
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

	print( tester(test_account.get_balance, 0) )
	print( tester(test_account.get_full_name, "Ally Checking Account") )
	print( tester(test_account.get_transactions, []) )

	print( tester(test_account.add_single_transaction, None, [None]) )
	print( tester(test_account.add_transactions, None, [[None]]) )


def tester( function, expected_value, params_lst=[]):
	""" Generic tester function, very simple. Produces string outputs for tests.
		Expects comparison to be performed with '=='.
		Should be later moved to a more generic "testing" file.

		function_pointer -> value -> parameter_list (optional) -> string
	"""
	"""
	NOTE: the following if is slightly more complicated. We are passing in a function POINTER
		As well as the expected value. So in essence we could just do "function() == expected_value"
		to determine if the function is working as expected. HOWEVER, this assumes that the
		function is not taking in ANY parameters. Hence why we need this strange "*params_lst" bit.
		The "*" is a special python shortcut that lets us convert a list in a parameter list. 
		Therefore, if params_lst is holding the value: [1,2,3]... then function(*params_lst) is 
		equivalent to function(1,2,3). 
		
		Additionally, function.__name__ abuses another python specialty in which there is
		'metadata' about functions in what are called "function attributes". You can find
		lists of these attributes online, but basically we can use them for non-typical
		use cases like testing output. 
	"""
	if (function(*params_lst) == expected_value):
		return function.__name__ + " passed"
	return function.__name__ + " FAILED. Expected " + function(*params_lst) + " to be equal to " + expected_value + "."
	

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
	
		

