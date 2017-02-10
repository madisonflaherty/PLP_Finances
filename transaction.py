"""
	transaction.py
	@author madison flaherty
	@author [YOUR_NAME_HERE]
	Simple bank transaction model
"""

import datetime as dt
import generic_testing as t

class Transaction:
	"""
	Simple transaction structure
	"""

	datetime = dt.datetime.now()
	amount = 0
	trans_type = ""
	description = ""

	def __init__(self, date, time, amount):
		""" string -> string -> string -> Transaction """

		""" NOTE: Here I am assuming that date is a string such as "2017-02-10" and
				time is a string such as "05:43:34". In this case I decided to store both in
				python's simple datetime object representation. Feel free to change this if
				you know a different or more convenient way! Also, not all bank transaction
				are actually recorded this way. We will ultimately be importing bank data
				into this so if you want to see how your bank does this now and change the
				representation now it might make your life a little easier later.
		"""
		self.datetime = dt.datetime.strptime(date + "-" + time, '%Y-%m-%d-%H:%M:%S')

		""" Note: as you can see in the parameter types I listed, I'm assuming that
			the 'amount' value we get will still be a string (likely from manual input or from
			a .csv file or so). So I am converting it from a string to a float (for now assume that
			a float is a number that supports decimal values if this is an unfamiliar term). 
			If you want to learn more about Python types check them out here:
				https://docs.python.org/3/library/stdtypes.html
		"""
		self.amount = float(amount)

	def get_datetime(self):
		""" None -> datetime """
		#STUBBED
		return

	def get_amount(self):
		""" None -> num """
		#STUBBED
		return

	def is_deposit(self):
		""" None -> boolean 
			return true if this transaction is a deposit (ie: adding to the total balance)
		"""
		#STUBBED
		return True

	def is_withdraw(self):
		""" None -> boolean 
			Convenience function for readability, returns true if a withdraw
		"""
		return not self.is_deposit()
	
	""" NOTE: There may or may not be many more methods that you are interested in adding here.
			If there's something you think will be particularly useful feel free to add it now!
	"""

"""
TESTING STRUCTURES
"""
def transaction_tests():
	"""Tests the transaction structure"""
	transaction = Transaction('2017-02-10','05:43:34','145.72')

	print( t.tester(transaction.get_datetime, dt.datetime.strptime('2017-02-10-05:43:34', '%Y-%m-%d-%H:%M:%S')) )
	print( t.tester(transaction.get_amount, 145.72) )
	
	print( t.tester(transaction.is_deposit, True) )
	print( t.tester(transaction.is_withdraw, False) )


if __name__ == "__main__":
	transaction_tests()
