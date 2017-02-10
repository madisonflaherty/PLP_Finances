
def tester( function, expected_value, params_lst=[]):
	""" Generic tester function, very simple. Produces string outputs for tests.
		Expects comparison to be performed with '=='.
		Should be later moved to a more generic "testing" file.

		function_pointer -> value -> parameter_list (optional) -> string
	"""
	"""
	NOTE: the following if is slightly more complicated. We are passing in a function REFERENCE
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
		return "passed: " + function.__name__
	return "FAILED: " + function.__name__ + " -> Expected " + str(function(*params_lst)) + " to be equal to " + str(expected_value) + "."
	

