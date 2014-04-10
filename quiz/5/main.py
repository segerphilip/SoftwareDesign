class Person():
	def __init__(self, name, date_of_birth):
		self.name = name
		self.date_of_birth = date_of_birth

class Employee(Person):
	def __init__(self, date_of_hire, salary, *args, **kwargs):
		super(Employee, self).__init__(*args, **kwargs)

		self.date_of_hire = date_of_hire
		self.salary = salary

	def earns_more_than(self, salary_level):
		if self.salary > salary_level:
			return True
		else:
			return False

class Manager(Employee):
	def __init__(self, direct_reports, *args, **kwargs):
		super(Person, self).__init__(*args, **kwargs)

		self.direct_reports = direct_reports

	def add_direct_report(self, new_report):
		self.direct_reports = new_report