a = 5
b = 7

a >= b  # False
a <= b  # True

c = a > b  # False
d = a < b  # True

e = a is b  # False
f = a is not b  # True

g = not e  # True

h = e and f  # False
j = e or f  # True

if e:
	print('e is true')
elif g:
	print('this one always will print')
else:
	print('e lied!')


