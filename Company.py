class Company:
	"""Represents any company employee."""

	def __init__(self, name, age):
		self.name = name
		self.age = age

class Boss(Company):

	def __init__(self, name, age, position = "Boss"):
		Company.__init__(self, name, age)
		self.position = position
	def tell(self):
		print("Position: {}\nName: {}\nAge: {}".format(self.position, self.name, self.age))

class Manager(Company):

	def __init__(self, name, age, days = 25, salary = 300000, position = "Manager"):
		Company.__init__(self, name, age)
		self.position = position
		self.salary = salary
		self.days = days

	def tell(self):
		print("Position: {}\nName: {}\nAge: {}\nWork Days: {}\nSalary: {}".format(self.position, self.name, self.age, self.days, self.salary))


class Staff(Company):

	def __init__(self, name, age, days = 21, salary = 150000, position = "Staff"):
		Company.__init__(self, name, age)
		self.position = position
		self.salary = salary
		self.days = days

	def tell(self):
		print("Position: {}\nName: {}\nAge: {}\nWork Days: {}\nSalary: {}".format(self.position, self.name, self.age, self.days, self.salary))



b = Boss('U Maung Khine', 20)

m = Manager('U Chit Maung', 40)

s = Staff('U Yaw Min Gyi', 30)

employees = [b, m, s]
for workers in employees:
	workers.tell()
	print()