	# <QUESTION 1>

	# Given a string, return the boolean True if it ends in "py", and False if not. Ignore Case.

	# <EXAMPLES>

	# endsDev("ilovepy") → True
	# endsDev("welovepy") → True
	# endsDev("welovepyforreal") → False
	# endsDev("pyiscool") → False

	# <HINT>

	# What was the name of the function we have seen which changes the case of a string?  Use your CLI to access the Python documentation and get help(str).
    
def endsPy(input):

	full = input
	last2 = full[-2:]
	if last2.casefold() == "py":
		print(f"{full} ends in py! ")
		return True
	else:
		return False

endsPy("Python")
endsPy("Pythpy")
endsPy("PythPY")
endsPy("Pythonpyy")
