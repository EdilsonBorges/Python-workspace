# Classes and Objects

class Person:
	__name = ''
	__email = ''

	def __init__(self, name, email):
		self.__name = name
		self.__email = email

	def set_name(self, name):
		self.__name = name

	def get_name(self):
		return self.__name

	def set_email(self, email):
		self.__email = email

	def get_email(self):
		return self.__email

	def toString(self):
		return '{} can be contacted at {}'.format(self.__name, self.__email)


brad = Person('Brad', 'brad@gmail.com')
# brad.set_name('Brad')
# brad.set_email('brad@gmail.com')
# print(brad.get_name(), '-', brad.get_email())
print(brad.toString())