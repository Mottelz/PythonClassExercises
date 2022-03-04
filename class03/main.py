from student import Student
from exercises import Course
from random import randint


def add_random_grade(s: Student):
	s.add_grade(randint(60, 100))


def main():
	oop = Course('OOP II', 'P02-001')
	oop.add_student('Jack Frost', '0001')
	oop.add_student('Doris Conway', '0002')
	oop.add_student('Alex Smith', '0003')

	for student in oop.students:
		for i in range(5):
			add_random_grade(student)
	print(oop)


if __name__ == '__main__':
	main()



