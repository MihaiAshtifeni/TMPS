# Lab.2 Topic: *Structural Design Patterns*

------
## Table of Contents

* [Objectives](#objectives)
* [Some Theory](#theory)
* [Main Tasks](#main-tasks)
* [Implementation](#implementation)
* [Conclusions](#conclusions)
* [Results](#Results)
* [Author](#author)
------
## Objectives:

__1. Study and understand the Structural Design Patterns.__

__2. As a continuation of the previous laboratory work, think about the functionalities that your system will need to provide to the user.__

__3. Implement some additional functionalities using structural design patterns.__

## Some Theory:

In software engineering, the Structural Design Patterns are concerned with how classes and objects are composed to form larger structures. Structural class patterns use inheritance to create a hierarchy of classes/abstractions, but the structural object patterns use composition which is generally a more flexible alternative to inheritance.

Some examples of this kind of design patterns are :

   * Adapter- Allows objects with incompatible interfaces to collaborate;
   * Bridge- Lets you split a large class, or a set of closely related classes into two separate hierarchies
   * Composite- Lets you compose objects into tree structures and then work with these structures as if they were individual objects;
   * Filter- Can combines multiple criteria to obtain single criteria.
   * Decorator- Lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors;
   * Facade- Wraps a complex sub-system with a simple abstraction.
   * Flyweight- Lets you fit more objects into the available amount of RAM by sharing common parts of state between multiple objects instead of keeping all the data in each object.
   * Proxy- Lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object;
   
   
## Main tasks :

__1. Study and understand the Structural Design Patterns.__

__2. Determine the additional functionalities of the system.__

__3. Based on the previous point, implement at least 3 structural design patterns in your project;__

## Implementation

This project illustrates the implementation of the following structural design patterns:
   * __Proxy__
   * __Decorator__
   * __Composite__
   

__1.Proxy__

~~~
from abc import ABCMeta,abstractmethod, abstractstaticmethod
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

p1 = Person()
p1.person_method()

p2 = ProxyPerson()
p2.person_method()
~~~

__2.Decorator__

Decorator is same as Proxy:

~~~
from abc import ABCMeta,abstractmethod, abstractstaticmethod

def mydecorator(function):
	def wrapper(*args, **kwargs):
  
		print("I am decorating your function!")
		return function(*args, **kwargs)

	return wrapper
  
@mydecorator
def hello(person):
	print(f"Hello {person}!")

hello("Mike")   # how work decoratot


#Practical Example #1 "Decorator" - Logging

def logged(function):
	def wrapperr(*args, **kwargs):
		value = function(*args, **kwargs)
		with open ('logfile.txt', 'a+') as f:
			fname = function.__name__
			print(f"{fname} returned value {value}") 
			f.write(f"{fname} returned value {value}")
		return value
	return wrapperr
@logged
def add(x, y):
	return x + y 

print(add(10,90)) 

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

print(myfunction(30000)) #here is not coment
~~~

__3.Composite__

~~~
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
~~~
## Results:
__1.Proxy__
~~~
I am a person!
I am the proxy functionality*
I am a person!
~~~

__2.Decorator__
~~~
I am decorating your function!
Hello Mike!
100
myfunction took 0.3432729244232178 seconds to execute!
<Big Namber (30000!)>
~~~

__3.Composite__
~~~
Parent Department
Parent Department Base Employees: 30
Accounting Department: 200
Development Department: 170
Total number of employees: 400
~~~

## Conclusions

The main goal of this laboratory work was to put into practice Structural Design Patterns.
After studying all the theory and putting it into practice in this laboratory work, 
I straighten my knowledge about Design Patterns, and namely about SDPs.
In short, they focus on how classes and objects can be composed into larger structures
and at the same time to keep these structures flexible and efficient. 
Another challenge that I have faced was to respect the project structure, but from my point of view, I managed to do it not so bad.

## Author: 

__Astifeni Mihai FAF-192__
