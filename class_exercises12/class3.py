'''Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. 
   These brackets must be close in the correct 
   order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.
'''

class Validparentices:
	def valid(s):
		dct = {'(':')', 
		
