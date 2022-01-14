class User():

	def __init__(self, firstName, lastName, age, street):
		self.firstName = firstName
		self.lastName = lastName
		self.age = age
		self.street = street

	def getFirstName(self):
		return self.firstName 

	def setFirstName(self,firstName):
		self.firstName = firstName

	def getLastName(self):
		return self.lastName

	def setLastName(self,lastName):
		self.lastName = lastName

	def getAge(self):
		return self.age 

	def setAge(self,age):
		self.age = age 

	def getStreet(self):
		return self.street 

	def setStreet(self,street):
		self.street = street 

	def print(self):
		print("===User===")
		print("Name: ", self.firstName + " " + self.lastName)
		print("Age: ", self.age)
		print("Street: ", self.street)
		