from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

	@abstractstaticmethod
	def person_method():
		"""Interface Method"""

class Student(IPerson):

	def __init__(self):
		self.name ="Basic Student Name"

	def person_method(self):
		print("You can start work like a Student, but first login ===>")

class Teacher(IPerson):

	def __init__(self):
		self.name = "Basic Teacher Name"

	def person_method(self):
		print("You can start work like a Teacher, but first login ===>")

class PersonFactory:

	@staticmethod
	def build_person(person_type):
		if person_type == "Student":
			return Student()
		if person_type == "Teacher":
			return Teacher()
		print("Invalid Type")
		return -1

if __name__ == "__main__":
	choice = input ("What tipe of person do you want to create?\n")
	person = PersonFactory.build_person(choice)
	person.person_method()


#############################################################################

class IPerson(metaclass=ABCMeta):
	def get_data():
		"""Implement in child class Singleton"""

class PersonSingleton(IPerson):

	__instance = None

	@staticmethod 
	def get_istance():
		if PersonSingleton.__instance == None:
			PersonSingleton("Default Name", 0)
			return PersonSingleton.__instance

	def __init__(self,status, name, password):
		if PersonSingleton.__instance != None:
			raise Exception("Singleton cannot be istantiated more than once")
		else:
			self.status = status
			self.name = name
			self.password = password
			PersonSingleton.__instance = self

	@staticmethod
	def print_data():
		print(f"Status: {PersonSingleton.__instance.status},  Name: {PersonSingleton.__instance.name},  Password: {PersonSingleton.__instance.password}")

if __name__ == "__main__":
	print("------------------------------------------")
	status = input("Login with your status Teacher/Student :\n")
	name = input("Name: \n")
	password = int(input("Password: \n"))
	Auntification = PersonSingleton(status, name, password)
	Auntification.print_data()



