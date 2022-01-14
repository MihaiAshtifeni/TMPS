# Lab.1 Topic: *Creational Design Patterns*

------
## Table of Contents

* [Objectives](#objectives)
* [Some Theory](#theory)
* [Main Tasks](#main-tasks)
* [Implementation](#implementation)
* [Results](#results)
* [Conclusions](#conclusions)
* [Author](#author)
------
## Objectives:

__1. Study and understand the Creational Design Patterns.__

__2. Choose a domain, define its main classes/models/entities and choose the appropriate instantiation mechanisms.__

__3. Use some creational design patterns for object instantiation in a sample project.__

## Some Theory:

In software engineering, the creational design patterns are the general solutions that deal with object creation, trying to create objects in a manner suitable to the situation. The basic form of object creation could result in design problems or added complexity to the design. Creational design patterns solve this problem by optimizing, hiding or controlling the object creation.

Some examples of this kind of design patterns are :

   * Singleton
   * Builder
   * Prototype
   * Object Pooling
   * Factory Method
   * Abstract Factory
   
## Main tasks 

__1. Choose an OO programming language and a suitable IDE or Editor;__

__2. Select a domain area for the sample project;__

__3. Define the main involved classes and think about what instantiation mechanisms are needed;__

__4. Based on the previous point, implement atleast 3 creational design patterns in your project;__

## Implementation 

__This project illustrates the implementation of the following creational design patterns:__
   * Singleton
   * Factory Method
   * Builder
 
__1.Singleton__

Singleton is a design pattern that restricts the instantiation of a class to one "single" instance. 

~~~
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
	password = int(input("Password\n"))
	Auntification = PersonSingleton(status, name, password)
	Auntification.print_data()

 ~~~


__2.Factory__

The idea of factory pattern is that subclasses are responsible to create instance of the class.
In this example, the factory methods are obtained by  


~~~

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
		print("I am a teacher")

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
       
~~~

__3.Builder__

Builder is a design pattern that allows to produce different objects using the same code and constructs complex objects step by step.


User:
~~~
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
~~~

UserBuilder:
 
~~~
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
~~~
Main of user bulder:
~~~
from User import User
from UserBuilder import UserBuilder

user = UserBuilder.item().withFirstName("Mihai").withLastName("Astifeni").withAge(21).liveInStreet("Studentilor 21").build()
user.print()
~~~



## Results

__1.Factory and Singleton__

~~~
What tipe of person do you want to create?
Student
You can start work like a Student, but first login ===>
------------------------------------------
Login with your status Teacher/Student :
Student
Name:
Mihai
Password:
1234
~~~

__2.Builder__

~~~
===User===
Name:  Mihai Astifeni
Age:  21
Street:  Studentilor 21
~~~


## Conclusions:

The main goal of this laboratory work was to put into practive Creational Design Patterns.
Generally speaking, design patterns are a very important field of computer science that is important in order to become a developper,
as design patterns are reusable in multiple projects and provide solutions that can help
define and build a good system architecture.

## Author: 

__Astifeni Mihai FAF-192__
