from abc import ABCMeta,abstractmethod, abstractstaticmethod

""" >>>>>>>>>>>>>>>>>>>>Proxy start<<<<<<<<<<<<<<<<<<<<<<<"""

class IPerson(metaclass=ABCMeta):
	@abstractstaticmethod
	def person_method():
		""" Interface Method"""

class Person(IPerson):
	def person_method(self):
		print("I am a person!")

class ProxyPerson(IPerson):
	def __init__(self):
		self.person = Person()

	def person_method(self):
		print("I am the proxy functionality*")
		self.person.person_method()

#p1 = Person()        # here is not coment******
#p1.person_method()
#
#p2 = ProxyPerson()
#p2.person_method()

""" >>>>>>>>>>>>>>>>>>>>Proxy end<<<<<<<<<<<<<<<<<<<<<<<"""

""" >>>>>>>>>>>>>>>>>>>>Decorator start<<<<<<<<<<<<<<<<<<<<<<<"""
def mydecorator(function):
	def wrapper(*args, **kwargs):
		print("I am decorating your function!")
		return function(*args, **kwargs)

	return wrapper
@mydecorator
def hello(person):
	print(f"Hello {person}!")

#hello("Mike")   #here is not coment*******



#Practical Example #1 "Decorator" - Logging

def logged(function):
	def wrapperr(*args, **kwargs):
		value = function(*args, **kwargs)
		with open ('logfile.txt', 'a+') as f:
			fname = function.__name__
			#print(f"{fname} returned value {value}")  #here is not coment******
			f.write(f"{fname} returned value {value}")
		return value
	return wrapperr
@logged
def add(x, y):
	return x + y 

# print(add(10,90)) #here is not coment******

# Practical Example #2 "Decorator" - Timing

import time

def timed(function):
	def wrapperrr(*args, **kwargs):
		before = time.time()
		value = function(*args, **kwargs)
		after = time.time()
		fname = function.__name__
		print(f"{fname} took {after - before} seconds to execute!")
		return value
	return wrapperrr
@timed
def myfunction(x):
	result = 1
	for i in range(1,x):
		result *= i
	return result

#print(myfunction(30000)) #here is not coment

""" >>>>>>>>>>>>>>>>>>>>Decorator end<<<<<<<<<<<<<<<<<<<<<<<"""
""" >>>>>>>>>>>>>>>>>>>>Composite start<<<<<<<<<<<<<<<<<<<<<<<"""

class IDepartment(metaclass=ABCMeta):
	@abstractmethod
	def __init__(self,employees):
		self.employees = employees

	@abstractstaticmethod
	def print_department():
		"""   impliment in child class  """


class Accounting(IDepartment):
	def __init__(self, employees):
		self.employees = employees

	def print_department(self):
		print(f"Accounting Department: {self.employees}")


class Development(IDepartment):
	def __init__(self, employees):
		self.employees = employees

	def print_department(self):
		print(f"Development Department: {self.employees}")


class ParentDepartment(IDepartment):
	def __init__(self, employees):
		self.employees = employees
		self.base_employees = employees
		self.sub_depts = []

	def add(self, dept):
		self.sub_depts.append(dept)
		self.employees += dept.employees  # numarul total de lucratori
		
	def print_department(self):
		print("Parent Department")
		print(f"Parent Department Base Employees: {self.base_employees}")
		for dept in self.sub_depts:
			dept.print_department()
		print(f"Total number of employees: {self.employees}")

dept1 = Accounting(200)
dept2 = Development(170)
parent_dept = ParentDepartment(30)
parent_dept.add(dept1)
parent_dept.add(dept2)

parent_dept.print_department()

""" >>>>>>>>>>>>>>>>>>>>Composite end<<<<<<<<<<<<<<<<<<<<<<<"""


		

