from student import Student


class Course:
	def __init__(self, title, course_id):
		self.title = title
		self.course_id = course_id
		self.students = []

	def add_student(self, name, id):
		self.students.append(Student(name, id))

	def __str__(self):
		out = ''
		for s in self.students:
			out += str(s)+'\n'
		return out
