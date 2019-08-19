#!/usr/bin/env python3
import sys
from collections import Counter

class Person(object):
	"""
	返回具有给定名称的 Person 对象
	"""
	def __init__(self, name):
		self.name = name
#		self.args = args

	def get_details(self):
		"""
		返回包含人名的字符串
		"""
		return self.name
	
	def get_grade(self):
	#	return self.args
		return 0		

class Student(Person):
	"""
	返回 Student 对象， 采用 name, branch, year 3 个参数
	"""
	
	def __init__(self, name, branch, year, args):
		Person.__init__(self, name)
		self.args = args
		self.branch = branch
		self.year = year
		
	def get_details(self):
		"""
		返回包含学生具体信息的字符串
		"""
		return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)
	
	def get_grade(self):
		word = Counter(self.args).most_common(4)
		n1 = 0
		n2 = 0
		for k, v in word:
			if k != "D":
				n1 += v
			else:
				n2 += v
		"""
		for item  in word:
			if item[0] != 'D':	#使用索引
				n1 += item[1]
			else:
				n2 += item[1] 
		"""
		print("Pass: {}, Fail: {}".format(n1, n2))
	

class Teacher(Person):
	"""
	返回 Teacher 对象，采用字符串列表作为参数
	"""

	def __init__(self, name, papers,args):
		Person.__init__(self, name)
		self.args = args
		self.papers = papers

	def get_details(self):
		return "{} teaches {}".format(self.name, ','.join(self.papers))

	def get_grade(self):
		word = Counter(self.args).most_common(4)
		s = []
		for k, v in word:
#			print("{} : {}".format(k, v ), end=",")
#		print()
			s.append("{}: {}".format(k, v))
		print(','.join(s))

#person1 = Person('Sachin', sys.argv[2])

person1 = Person("Sachin")
if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("USE: {} student|teacher  AABBBCCDDC".format(sys.argv[0]))
		sys.exit(-1)
	else:
		if sys.argv[1] == "student":
			student1 = Student('Kushal', 'CSE', 2005, sys.argv[2])
			student1.get_grade()
		else:
			teacher1 = Teacher('Prashad', ['C', 'C++'], sys.argv[2])
			teacher1.get_grade()
#person1 = Person("Sachin")
#student1 = Student("Kushal","CSE", 2005)
#teacher1 = Teacher("Prashad", ["C", "C++"])

#print(person1.get_details())
#print(student1.get_details())
#print(teacher1.get_details())


