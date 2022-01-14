from User import User

class UserBuilder():

	def __init__(self):
		self.firstName = ""
		self.lastName = ""
		self.age = 0
		self.street = ""

	@staticmethod
	def item():
		return UserBuilder()

	def withFirstName(self, name):
		self.firstName = name 
		return self

	def withLastName(self, name):
		self.lastName = name
		return self

	def withAge(self, age):
		self.age = age 
		return self

	def liveInStreet(self, street):
		self.street = street 
		return self

	def build(self):
		return User(self.firstName, 
					self.lastName,
					self.age,
					self.street) 