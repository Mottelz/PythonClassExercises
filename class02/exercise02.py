# Create a function that takes in a number
# and returns all the even numbers from 0 to the given number
def get_evens(number):
	out = []
	for n in range(number):
		if n % 2 == 0:
			out.append(n)
	return out


# Call the function and store the result
evens = get_evens(10)
# Print the list you got in the last question backwards
print(evens[::-1])
