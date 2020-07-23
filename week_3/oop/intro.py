"""
OBJECT ORIENTED PROGRAMMING
	- Programming paradigm where different components of a computer program are modeled after real-world objects

	* Object -  anything that has some characteristics (state) and can perform a function (behaviour)

	Why use OOP paradigm
		- Reusability - A computer program is written in the form of objects and classes, which can be reused in other projects as well
		- Highly maintainable code, through OOP's modular programming approach
		- Through the modular approach, you can easily debug a section without affecting the entire project/code
		- Data encapsulation - adds an extra layer of security to the program developed using the object-oriented approach

	CLASS
		- Serves as a blueprint for the object

"""

class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
