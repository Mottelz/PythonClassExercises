def greet():
	print('hello')


def greet_by_name(name='joke'):
	print(f'hello {name}')


def get_factorial(number):
	output = number
	for i in range(1, number):
		output *= i
	return output


a = get_factorial(5)
print(a)
