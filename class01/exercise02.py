# 1. Create a list with at least three numbers on it
a = [12, 3, 4546, 809, 190324, 875432098]

# 2. Compare the first and last number in your list and store the resulting boolean in a variable
b = a[0] > a[-1]


# 3. Write an if statement that uses your boolean from step 2. If it's true print out a happy message otherwise print out a sad one.
if b:
	print('hooray!')
else:
	print('boo hoo :(')
