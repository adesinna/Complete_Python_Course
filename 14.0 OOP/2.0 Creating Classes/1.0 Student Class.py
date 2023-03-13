class Student:
	def __init__(self, name: str, id: str, faculty: str, department: str):  # any attribute here must be given to the object when initializing.

		assert int(id) > 0  # this is to make sure id number is greater than zero

		self.name = name
		self.id = id
		self.faculty = faculty
		self.department = department

		self.admitted = False  # these are inner attributes, that do not need to be declared when construction

	def admit(self):  # this is a method
		self.admitted = True


student_001 = Student(name='Adesina', id='001', faculty='science', department='mathematics')

print(student_001.name)
print(student_001.admitted)
print(student_001.id)
print(student_001.faculty)
student_001.admit()
print(student_001.admitted)